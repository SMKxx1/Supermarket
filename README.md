# Supermarket
## Modules Used
```
import pymysql
import hashlib
import os
import time
import getpass
import platform 
import pandas
from tabulate import tabulate
import datetime
```
# Mysql
## __Products Table__


| Field | Type          | Null | Key | Default | Extra          |
|-------|---------------|------|-----|---------|----------------|
| id    | int(11)       | NO   | PRI | NULL    | auto_increment |
| item  | varchar(500)  | YES  |     | NULL    |                |
| type  | varchar(50)   | YES  |     | NULL    |                |
| qty   | int(11)       | YES  |     | NULL    |                |
| price | decimal(20,2) | YES  |     | NULL    |                |

### __Values__

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
