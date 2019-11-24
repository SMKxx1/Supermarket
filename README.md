# Supermarket
## Modules Used
```
import pymysql
import hashlib
import os
import time
import platform 
import pandas
from tabulate import tabulate
import datetime
```
### **import pymysql**
* [pymysql](https://pypi.org/project/PyMySQL/) - For MYSQL connection
```
conn = pymysql.connect(
    host = "localhost",
    port = 3306,
    user = "root",
    passwd = "1234",
    database = "Project"
)

c = conn.cursor()
```
Please ignore `port = 3306` argument.

`passwd = "1234"` is the same as `password = "1234"`.


### __import hashlib__
* [hashlib](https://pypi.org/project/hashlib/) - For hashing/encoding the password
```
def encoder(password):
    password = hashlib.md5(password.encode())
    password = password.hexdigest()
    return password
```
Creating a Function called encoder so that we can cut time in encoding passwords.

`password = hashlib.md5(password.encode())` here `hashlib.md5` is used to convert the password
to a md5 hash but it only works with utf-8 strings and since python uses unicode to store its strings
we will have to convert it to utf-8 using the command `.encode()`. After that the password will become a
md5 memory object so in order to convert it back to a string `.hexdigest()` is used.


### __import os__
* [os](https://docs.python.org/3.7/library/os.html) - For clearing the screen
```
def clear():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')
```
There are a million things you can do with os module but here we will be using it to clear the screen.
The clear screen command is different on windows, mac and linux so we use the platform module to find the 
operating system. Then pass a command corresponding to the operating system being used.
* Windows - `os.system('cls')`
* Mac/Linux - `os.system('clear')`


### __import time__
* [time](https://docs.python.org/3.7/library/time.html) - For sleep function
```
time.sleep(1)
```
`time.sleep()` takes a number as an argument. This number is the amount of seconds that the program will freez for.


### __import platform__
* [platform](https://docs.python.org/3.7/library/platform.html) - For identifying the operating system
```
def clear():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')
```
This module is used to find out the operating system running the program.

### __from tabulate import tabulate__
* [tabulate](https://pypi.org/project/tabulate/) - For printing the DataFrame
```
print(tabulate(cart, headers='keys', showindex=False, tablefmt='fancy_grid'))
```
This module help Pretty-print tabular data in Python. It is not present in python by default but needs to be installed
if python environment is setup on the computer then type `python -m pip install tabulate` in the windows terminal.
Or else copy the tabulate file from the github repository and paste it in `C:\Users\admin\AppData\Local\Programs\Python\Python37\Lib`

# Mysql
## __Products Table__


| Field | Type          | Null | Key | Default | Extra          |
|-------|---------------|------|-----|---------|----------------|
| id    | int(11)       | NO   | PRI | NULL    | auto_increment |
| item  | varchar(500)  | YES  |     | NULL    |                |
| type  | varchar(50)   | YES  |     | NULL    |                |
| qty   | int(11)       | YES  |     | NULL    |                |
| price | decimal(20,2) | YES  |     | NULL    |                |


__To create the table copy and paste the following command__
```
CREATE TABLE 'products' (
'id' int(11) PRIMARY KEY AUTO_INCREMENT,
'item' varchar(500),
'type' varchar(50),
'qty' int(11),
'price' decimal(20,2));
```


### __Data__

__To insert values copy and paste the following command__
```
INSERT INTO products(id,item,type,qty,price) VALUES (NULL,'Sunfeast Dark Fantasy','Biscuits',320,40.00);
INSERT INTO products(id,item,type,qty,price) VALUES (NULL,'Sunfeast Marie Light Oats','Biscuits',400,14.00);
INSERT INTO products(id,item,type,qty,price) VALUES (NULL,'Britannia Marie Gold','Biscuits',120,30.00);
INSERT INTO products(id,item,type,qty,price) VALUES (NULL,'Cadbury Oreo Vanilla','Biscuits',330,30.00);
INSERT INTO products(id,item,type,qty,price) VALUES (NULL,'Cadbury Oreo Strawberry','Biscuits',90,30.00);
INSERT INTO products(id,item,type,qty,price) VALUES (NULL,'Bingo Potato Chips Masala','Chips',50,20.00);
INSERT INTO products(id,item,type,qty,price) VALUES (NULL,'Bingo Mad Angles','Chips',220,20.00);
INSERT INTO products(id,item,type,qty,price) VALUES (NULL,'Lays Potato Chips American Style Cream and Onion','Chips',500,30.00);
INSERT INTO products(id,item,type,qty,price) VALUES (NULL,'Lays Potato Chips Indias Magic Masala','Chips',190,30.00);
INSERT INTO products(id,item,type,qty,price) VALUES (NULL,'Act II Jalapeno Nachoz','Chips',60,60.00);
INSERT INTO products(id,item,type,qty,price) VALUES (NULL,'Flavours of Calicut Kerala Banana Chips','Chips',30,500.00);
INSERT INTO products(id,item,type,qty,price) VALUES (NULL,'Pringles Sour Cream and Onion','Chips',300,100.00);
INSERT INTO products(id,item,type,qty,price) VALUES (NULL,'Pringles Potato Crisps Original','Chips',200,100.00);
INSERT INTO products(id,item,type,qty,price) VALUES (NULL,'Cornitos Nachos Crisps, Sizzlin Jalapeno','Chips',200,40.00);
INSERT INTO products(id,item,type,qty,price) VALUES (NULL,'Almonds 500g','Dried Fruits',40,500.00);
INSERT INTO products(id,item,type,qty,price) VALUES (NULL,'Cashews 200g','Dried Fruits',40,220.00);
INSERT INTO products(id,item,type,qty,price) VALUES (NULL,'Peanuts 500g','Dried Fruits',50,100.00);
INSERT INTO products(id,item,type,qty,price) VALUES (NULL,'Pistachios 200g','Dried Fruits',20,320.00);
INSERT INTO products(id,item,type,qty,price) VALUES (NULL,'Walnut Without Shell 400g','Dried Fruits',50,700.00);
INSERT INTO products(id,item,type,qty,price) VALUES (NULL,'Inshell Walnuts 400g','Dried Fruits',20,600.00);
INSERT INTO products(id,item,type,qty,price) VALUES (NULL,'Dates 400g','Dried Fruits',40,300.00);
INSERT INTO products(id,item,type,qty,price) VALUES (NULL,'Tata Tea Gold 1kg','Beverage',300,380.00);
INSERT INTO products(id,item,type,qty,price) VALUES (NULL,'Davidoff Coffee Rich Aroma 100g','Beverage',30,500.00);
INSERT INTO products(id,item,type,qty,price) VALUES (NULL,'Tropicana Cranberry Delight Fruit Juice 1000ml','Beverage',10,130.00);
INSERT INTO products(id,item,type,qty,price) VALUES (NULL,'Tropicana Orange Juice 1000ml','Beverage',20,130.00);
INSERT INTO products(id,item,type,qty,price) VALUES (NULL,'Tropicana Mixed Fruit Juice 1000ml','Beverage',10,130.00);
INSERT INTO products(id,item,type,qty,price) VALUES (NULL,'Cadbury Dairy Milk Silk Oreo 60g','Sweets',20,100.00);
INSERT INTO products(id,item,type,qty,price) VALUES (NULL,'Ferrero Rocher Chocolate 16 Pcs','Sweets',15,500.00);
INSERT INTO products(id,item,type,qty,price) VALUES (NULL,'Toblerone Swiss Milk Chocolate 100g','Sweets',50,300.00);
INSERT INTO products(id,item,type,qty,price) VALUES (NULL,'Amul 75% Bitter Chocolate 150g','Sweets',30,125.00);
```

| id | item                                             | type         | qty  | price  |
|----|--------------------------------------------------|--------------|------|--------|
|  1 | Sunfeast Dark Fantasy                            | Biscuits     |  320 |  40.00 |
|  2 | Sunfeast Marie Light Oats                        | Biscuits     |  400 |  14.00 |
|  3 | Britannia Marie Gold                             | Biscuits     |  120 |  30.00 |
|  4 | Cadbury Oreo Vanilla                             | Biscuits     |  330 |  30.00 |
|  5 | Cadbury Oreo Strawberry                          | Biscuits     |   90 |  30.00 |
|  6 | Bingo Potato Chips Masala                        | Chips        |   50 |  20.00 |
|  7 | Bingo Mad Angles                                 | Chips        |  220 |  20.00 |
|  8 | Lays Potato Chips American Style Cream and Onion | Chips        |  500 |  30.00 |
|  9 | Lays Potato Chips Indias Magic Masala            | Chips        |  190 |  30.00 |
| 10 | Act II Jalapeno Nachoz                           | Chips        |   60 |  60.00 |
| 11 | Flavours of Calicut Kerala Banana Chips          | Chips        |   30 | 500.00 |
| 12 | Pringles Sour Cream and Onion                    | Chips        |  300 | 100.00 |
| 13 | Pringles Potato Crisps Original                  | Chips        |  200 | 100.00 |
| 14 | Cornitos Nachos Crisps, Sizzlin Jalapeno         | Chips        |  200 |  40.00 |
| 15 | Almonds 500g                                     | Dried Fruits |   40 | 500.00 |
| 16 | Cashews 200g                                     | Dried Fruits |   40 | 220.00 |
| 17 | Peanuts 500g                                     | Dried Fruits |   50 | 100.00 |
| 18 | Pistachios 200g                                  | Dried Fruits |   20 | 320.00 |
| 19 | Walnut Without Shell 400g                        | Dried Fruits |   50 | 700.00 |
| 20 | Inshell Walnuts 400g                             | Dried Fruits |   20 | 600.00 |
| 21 | Dates 400g                                       | Dried Fruits |   40 | 300.00 |
| 22 | Tata Tea Gold 1kg                                | Beverage     |  300 | 380.00 |
| 23 | Davidoff Coffee Rich Aroma 100g                  | Beverage     |   30 | 500.00 |
| 24 | Tropicana Cranberry Delight Fruit Juice 1000ml   | Beverage     |   10 | 130.00 |
| 25 | Tropicana Orange Juice 1000ml                    | Beverage     |   20 | 130.00 |
| 26 | Tropicana Mixed Fruit Juice 1000ml               | Beverage     |   10 | 130.00 |
| 27 | Cadbury Dairy Milk Silk Oreo 60g                 | Sweets       |   20 | 100.00 |
| 28 | Ferrero Rocher Chocolate 16 Pcs                  | Sweets       |   15 | 500.00 |
| 29 | Toblerone Swiss Milk Chocolate 100g              | Sweets       |   50 | 300.00 |
| 30 | Amul 75% Bitter Chocolate 150g                   | Sweets       |   30 | 125.00 |


## __Purchase Table__
| Field       | Type          | Null | Key | Default | Extra          |
|-------------|---------------|------|-----|---------|----------------|
| purchase_id | int(11)       | NO   | PRI | NULL    | auto_increment |
| date        | date          | YES  |     | NULL    |                |
| item_qty    | varchar(5000) | YES  |     | NULL    |                |
| price       | decimal(20,2) | YES  |     | NULL    |                |
| tax         | decimal(20,2) | YES  |     | NULL    |                |
| total_price | decimal(20,2) | YES  |     | NULL    |                |


__To create the table copy and paste the following command__
```
CREATE TABLE 'purchase' (
'purchase_id' int(11) PRIMARY KEY AUTO_INCREMENT,
'date' date,
'item_qty' varchar(5000),
'price' decimal(20,2),
'tax' decimal(20,2),
'total_price' decimal(20,2));
```
