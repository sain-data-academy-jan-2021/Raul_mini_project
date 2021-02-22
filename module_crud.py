import csv
from os import write
import module_print
import pymysql
from prettytable import from_db_cursor
    

# --- DATABASES CRUD MODULES --- 
def execute_sql(connection, sql):
    cursor = connection.cursor()
    cursor.execute(sql)
    cursor.close()
    connection.commit()

# --- Products functions ---

def print_products(connection):
    cursor = connection.cursor()
    cursor.execute('SELECT products_id, product_name, price FROM Products')
    mytable = from_db_cursor(cursor)
    print(mytable)

def update_product(connection):
    product_select = input('What product would you like to update? \n')
    new_name = input('What would you like to updated to \n Press enter to continue \n')
    if new_name == '' :
        pass 
    else:
        cursor = connection.cursor()
        cursor.execute(f'UPDATE Products SET product_name = "{new_name}" WHERE products_id = "{product_select}"')
    new_price = input('Please enter a price for the product \n Press enter to continue \n')
    if new_price == '' :
        pass
    else:
        cursor = connection.cursor()
        cursor.execute(f'UPDATE Products SET price = "{new_price}" WHERE products_id = "{product_select}"')
    cursor.close()
    connection.commit()

def delete_product(connection):
    delete_product = int(input('What product would you like to delete? \n'))
    sql = (f'DELETE FROM Products WHERE products_id = "{delete_product}"')
    execute_sql(connection, sql)

def add_product(connection):
    new_product = input("What product would you like to add? \n").title()
    while True:
        try:
            product_price = float(input("What is the price of the product? \n"))
            break
        except ValueError:
            print('Please enter a number')
    sql = (f'INSERT INTO Products (product_name, price) VALUES ("{new_product}", {product_price})')
    execute_sql(connection, sql)

# ---- Couriers Functions ----
def print_couriers(connection):
    cursor = connection.cursor()
    cursor.execute('SELECT couriers_id, courier_name, phone FROM Couriers')
    mytable = from_db_cursor(cursor)
    print(mytable)
    

def update_courier(connection):
    courier_select = input('What courier would you like to update? \n')
    new_name = input('What would you like to updated to \n Press enter to continue \n')
    if new_name == '' :
        pass 
    else:
        cursor = connection.cursor()
        cursor.execute(f'UPDATE Couriers SET courier_name = "{new_name}" WHERE couriers_id = "{courier_select}"')
    new_phone = input('Please enter a phone for the courier \n Press enter to continue \n')
    if new_phone == '' :
        pass
    else:
        cursor = connection.cursor()
        cursor.execute(f'UPDATE Couriers SET phone = "{new_phone}" WHERE couriers_id = "{courier_select}"')
    cursor.close()
    connection.commit()

def add_courier(connection):
    new_courier = input("What is the name of the courier you would like to add? \n").title()
            # take the valuea and see if it meets the pattern values ether numeral or spaces, is it between len less than 12
    courier_phone = input("What is the phone number of the courier? \n")
    sql = (f'INSERT INTO Couriers (courier_name, phone) VALUES ("{new_courier}", "{courier_phone}")')
    execute_sql(connection, sql)

def delete_courier(connection):
    del_courier = int(input('What courier would you like to delete? \n'))
    sql = (f'DELETE FROM Couriers WHERE couriers_id = "{del_courier}" ')
    execute_sql(connection, sql)
    
# ---- ORDERS FUNCTIONS -----

def print_orders(connection):
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM Orders')
    mytable = from_db_cursor(cursor)
    print(mytable)

def read_orders_db(connection):
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM Orders')
    order_rows = cursor.fetchall()
    for row in order_rows:
        print(row)
    cursor.close()
    
def read_couriers_db(connection):
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM Couriers')
    order_rows = cursor.fetchall()
    for row in order_rows:
        print(row)
    cursor.close()

def read_products_db(connection):
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM Products')
    order_rows = cursor.fetchall()
    for row in order_rows:
        print(row)
    cursor.close()

def add_order_to_db(connection):
    new_name = input('Please enter your full name for the order \n').capitalize()
    cust_address = input('Please enter a delivery address \n')
    phone = input('Enter your phone number \n')
    courier = add_courier_to_order(connection)
    live_status = 'In progress'
    items = add_products_to_order(connection)
    execute_sql(connection, f"INSERT INTO Orders (full_name, c_address, phone_number, courier, live_status) VALUES ('{new_name}', '{cust_address}', '{phone}', '{courier}', '{live_status}')")
    order_id = execute_sql_select(connection, 'SELECT max(order_id) FROM Orders')[0][0]
    for item in items:
        execute_sql(connection, f"INSERT INTO basket (order_id, products_id) VALUES ( '{order_id}', '{item}')")

def execute_sql_select(connection, sql):
    cursor = connection.cursor()
    cursor.execute(sql)
    cursor.close()
    return cursor.fetchall()

def add_courier_to_order(connection):
    # read_couriers_db(connection)
    print_couriers(connection)
    select_ids = []
    for row in execute_sql_select(connection, f'SELECT couriers_id FROM Couriers'):
        select_ids.append(row[0])
    while True:
        sel_courier = int(input('Please select a courier from the list \n'))
        if sel_courier in select_ids:
            return sel_courier
        else:
            continue

def add_products_to_order(connection):
    print_products(connection)
    # read_products_db(connection)
    select_ids = []
    select_product = []
    for row in execute_sql_select(connection, f'SELECT products_id FROM Products'):
        select_ids.append(row[0])
    while True:
        pick_product = int(input('Please select a product from the list \nPress 0 to exit \n'))
        if pick_product in select_ids:
            select_product.append(pick_product)
            continue
        elif pick_product == 0:
            break
        else:
            continue
    return select_product

def delete_from_db(connection):
    select_ids = [id[0] for id in execute_sql_select(connection, 'SELECT order_id FROM Orders')]
    while True:
        read_orders_db(connection)
        id = int(input('Please an Order to delete! \n'))
        if id in select_ids:
            execute_sql(connection, f'DELETE FROM basket WHERE order_id = {id}')
            execute_sql(connection, f'DELETE FROM Orders WHERE order_id = {id}')
            break
        else:
            print('Option selected is invalid')
# delete from basket and delete from orders first in basket and then in orders