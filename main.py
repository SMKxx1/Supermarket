import pymysql
import hashlib
import os
import time
import platform 
import pandas
from tabulate import tabulate
import datetime

def clear():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

conn = pymysql.connect(
    host = "localhost",
    port = 3306,
    user = "root",
    passwd = "1234",
    database = "store"
)

c = conn.cursor()

def update_df(cart):
    # update table products set 'qty' = ? where item like ?;
    command = ""
    for x, y in zip(cart['Name'], cart['Quantity']):
        command = f"UPDATE products SET qty = qty - %s WHERE item = %s;"
        paras = ( int(y), x)
        c.execute(command, paras)

def create_receipt():
    products = pandas.read_sql("SELECT * FROM products;", conn)
    cart = pandas.DataFrame(columns=['Item No','Name','Type','Quantity','Price'])
    item_no = 0
    try:
        while True:
            print(tabulate(products,
                           headers=['Item No','Name','Type','Quantity','Price'],
                           showindex=False,
                           tablefmt='psql'))
            print()
            print("CART")
            print(tabulate(cart,
                           headers='keys',
                           showindex=False,
                           tablefmt='fancy_grid'))
            item = int(input("Enter Item number: "))
            if item > 30:
                print("Invalid Value")
                input()
                clear()
            else:
                qty = int(input("Enter the quantity: "))
                pname = products.loc[int(item) - 1]['item']
                if qty > int(products.loc[int(item) - 1]['qty']):
                    existing_qty = int(products.loc[int(item) - 1]['qty'])
                    print(f"Not Enough {pname} in stock. Only {existing_qty} left")
                    input()
                    clear()
                else:
                    if products.loc[int(item) - 1]['item'] in list(cart['Name']):
                        products.loc[products.id == item, 'qty'] = products.loc[int(item) - 1]['qty'] - qty
                        cart.loc[cart.Name == products.loc[int(item) - 1]['item'], 'Quantity'] = cart.loc[cart.Name == products.loc[int(item) - 1]['item'], 'Quantity'] + qty
                        cart.loc[cart.Name == products.loc[int(item) - 1]['item'], 'Price'] = cart.loc[cart.Name == products.loc[int(item) - 1]['item'], 'Price'] + (qty * products.loc[int(item) - 1]['price'])
                        clear()
                    else:
                        item_no += 1
                        products.loc[products.id == item, 'qty'] = products.loc[int(item) - 1]['qty'] - qty
                        dic = {
                            'Item No': item_no,
                            'Name': products.loc[int(item) - 1]['item'],
                            'Type': products.loc[int(item) - 1]['type'],
                            'Quantity': qty,
                            'Price': (products.loc[int(item) - 1]['price']) * qty}
                        cart = cart.append(dic,
                                           ignore_index=True,
                                           sort=False)
                        clear()
    except KeyboardInterrupt:
        loop = False
        while loop == False:
            loop = True
            confirmation = input("\n[y/n] Confirm Purchase? ")
            if confirmation == 'y':
                update_df(cart)
                generate_receipt(cart)
            elif confirmation == 'n':
                pass
            else:
                print("Invalid Input")
                loop = False

def generate_receipt(cart):
    item_qty = {}
    for i, x in zip(cart['Name'], cart['Quantity']):
        item_qty[i] = x
    gst = lambda y: ((y/100) * 18)
    Tax = gst(cart['Price'])

    dic = {
        'Item No': cart['Item No'],
        'Item Name': cart['Name'],
        'Quantity': cart['Quantity'],
        'Price': cart['Price'],
        'Tax': Tax,
        'Final Price': cart['Price'] + Tax
    }
    receipt = pandas.DataFrame(dic)

    footer = {
        'Item No': None,
        'Item Name': 'Total Price',
        'Quantity': None,
        'Price': sum(receipt['Price']),
        'Tax': sum(receipt['Tax']),
        'Final Price': sum(receipt['Final Price'])}

    receipt = receipt.append(footer,
                             ignore_index=True,
                             sort=False)
    clear()
    print("RECEIPT")
    print(tabulate(receipt,
                   headers='keys',
                   showindex=False,
                   tablefmt='grid',
                   numalign='right'))
    input()
    date = datetime.date.today()
    price = footer['Price']
    tax = footer['Tax']
    TP = footer['Final Price']
    command = f"INSERT INTO purchase values (NULL, %s, %s, %s, %s, %s)"
    paras = (date, str(item_qty), price, tax, TP)
    c.execute(command, paras)
    conn.commit()
    
def view_history():
    try:
        while True:
            purchase = pandas.read_sql("SELECT * FROM purchase;",
                                       conn,
                                       index_col=None)
            products = pandas.read_sql("SELECT * FROM products;",
                                       conn,
                                       index_col=None)
            print(tabulate(purchase,
                           headers="keys",
                           showindex=False,
                           tablefmt="grid"))
            purchase_id = int(input("Enter the purchase id: "))
            for i in purchase.loc[purchase.purchase_id == purchase_id, "item_qty"]:
                dic1 = eval(i)
            Item_name = []
            Quantity = []
            for x, y in zip(dic1.keys(), dic1.values()):
                Item_name.append(x)
                Quantity.append(y)
            price = []
            price1 = []
            for i in Item_name:
                p = int(products.loc[products.item == i]["price"])
                price1.append(p)
            for i, _ in enumerate(price1):
                price.append(price1[i] * Quantity[i])
            Tax = []
            for i in price:
                Tax.append(round((i/100)*18, 2))
            FP = []
            for z, i in enumerate(price):
                FP.append(price[z]+Tax[z])
            dic = {
                'Item Name': Item_name,
                'Quantity': Quantity,
                'Price': price,
                'Tax': Tax,
                'Final Price': FP
            }
            receipt = pandas.DataFrame(data = dic,
                                       columns=['Item Name','Quantity','Price','Tax','Final Price'])

            footer = {
                'Item Name': 'Total Price',
                'Quantity': None,
                'Price': sum(receipt['Price']),
                'Tax': sum(receipt['Tax']),
                'Final Price': sum(receipt['Final Price'])}

            receipt = receipt.append(footer,
                                     ignore_index=True,
                                     sort=False)

            print(tabulate(receipt,
                           headers='keys',
                           tablefmt="grid",
                           showindex=False))

            graph = input("See graph?? [y/n] ")

            if graph.lower() == 'y':
                import matplotlib.pyplot as plt
                plt.pie(receipt['Price'][:-1], labels= receipt['Item Name'][:-1], autopct='%.2f%%',shadow=True)
                plt.title("Purchases")
                plt.show()

    except KeyboardInterrupt:
        pass


def main():
    clear()
    try:
        while True:
            print("""
    Enter your choice:
        1. Create Receipt
        2. View History
        3. Exit""")
            opt = input("> ")
            if opt == '1':
                create_receipt()
                clear()
            elif opt == '2':
                view_history()
                clear()
            else:
                break
    except KeyboardInterrupt:
        exit()

main()
conn.close()