import csv
from os import write
import module_print
import pymysql
from prettytable import from_db_cursor
    

# ============= DATABASES --- CRUD  ============== 


# ============= SQL exec statments ============== 

def execute_sql(connection, sql):
    cursor = connection.cursor()
    cursor.execute(sql)
    cursor.close()
    connection.commit()

def execute_sql_select(connection, sql):
    cursor = connection.cursor()
    cursor.execute(sql)
    cursor.close()
    return cursor.fetchall()

def execute_sql_select_join(connection, sql):
    cursor = connection.cursor()
    return cursor.execute(sql)
    

def read_orders_db(connection):
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM Orders')
    order_rows = cursor.fetchall()
    for row in order_rows:
        print(row)
    cursor.close()
# Test

def read_products_db(connection):
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM Products')
    order_rows = cursor.fetchall()
    for row in order_rows:
        print(row)
    cursor.close()

# ============= Print functions ============= 
def print_database(connection, table):
    cursor = connection.cursor()
    cursor.execute(f'SELECT*FROM {table}')
    mytable = from_db_cursor(cursor)
    print(mytable)

def print_orders(connection):
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM Orders')
    mytable = from_db_cursor(cursor)
    print(mytable)

# ============= Products functions ============= 

def update_product(connection):
    product_select = input('What product would you like to update? \n')
    new_name = input('What would you like to updated to\nPress enter to continue \n')
    if new_name == '' :
        pass 
    else:
        execute_sql(connection, f'UPDATE Products SET product_name = "{new_name}" WHERE products_id = "{product_select}"')
    new_price = float(input('Please enter a price for the product\nPress enter to continue\n'))
    if new_price == '' :
        pass
    else:
        execute_sql(connection, f'UPDATE Products SET price = {new_price} WHERE products_id = "{product_select}"')

def delete_product(connection):
    while True:
        try:
            delete_product = int(input('What product would you like to delete? \n'))
            break
        except IndexError:
            print('Product selected does not exist')
    sql = (f'DELETE FROM Products WHERE products_id = "{delete_product}"')
    execute_sql(connection, sql)

def add_product(connection):
    new_product = input("What product would you like to add? \n").title()
    while True:
        try:
            product_price = float(input("What is the price of the product? \n"))
            break
        except ValueError:
            print('Please enter a price/number')
    sql = (f'INSERT INTO Products (product_name, price) VALUES ("{new_product}", {product_price})')
    execute_sql(connection, sql)


# ============= Couriers Functions ============= 


def update_courier(connection):
    courier_select = input('What courier would you like to update? \n')
    new_name = input('What would you like to updated to \n Press enter to continue \n')
    if new_name == '' :
        pass 
    else:
        execute_sql(connection,f'UPDATE Couriers SET courier_name = "{new_name}" WHERE couriers_id = "{courier_select}"')
    new_phone = input('Please enter a phone for the courier \n Press enter to continue \n')
    if new_phone == '' :
        pass
    else:
        execute_sql(connection,f'UPDATE Couriers SET phone = "{new_phone}" WHERE couriers_id = "{courier_select}"')


def add_courier(connection):
    new_courier = input("What is the name of the courier you would like to add? \n").title()
    courier_phone = input("What is the phone number of the courier? \n")
    sql = (f'INSERT INTO Couriers (courier_name, phone) VALUES ("{new_courier}", "{courier_phone}")')
    execute_sql(connection, sql)

def delete_courier(connection):
    del_courier = int(input('What courier would you like to delete? \n'))
    sql = (f'DELETE FROM Couriers WHERE couriers_id = "{del_courier}"')
    execute_sql(connection, sql)


# ============= ORDERS FUNCTIONS ============= 


def add_order_to_db(connection):
    # i'm 
    new_name = input('Please enter your full name for the order\n').capitalize()
    cust_address = input('Please enter a delivery address\n')
    phone = input('Enter your phone number\n')
    courier = add_courier_to_order(connection)
    live_status = 'In progress'
    items = add_products_to_order(connection)
    execute_sql(connection, f"INSERT INTO Orders (full_name, c_address, phone_number, courier, live_status) VALUES ('{new_name}', '{cust_address}', '{phone}', '{courier}', '{live_status}')")
    order_id = execute_sql_select(connection, 'SELECT max(order_id) FROM Orders')[0][0]
    for item in items:
        execute_sql(connection, f"INSERT INTO Basket (order_id, products_id) VALUES ( '{order_id}', '{item}')")


def add_courier_to_order(connection):
    print_database(connection, 'Couriers')
    select_ids = []
    for row in execute_sql_select(connection, f'SELECT couriers_id FROM Couriers'):
        select_ids.append(row[0])
    while True:
        sel_courier = int(input('Please select a courier from the list \n'))
        if sel_courier in select_ids:
            return sel_courier
        elif sel_courier not in select_ids:
            print('Invalid option selected')
        else:
            continue

def add_products_to_order(connection):
    print_database(connection, 'Products')
    select_ids = []
    select_product = []
    for row in execute_sql_select(connection, f'SELECT products_id FROM Products'):
        select_ids.append(row[0])
    while True:
        pick_product = int(input('Please select a product from the list\nPress 0 to exit \n'))
        if pick_product in select_ids:
            select_product.append(pick_product)
            continue
        elif pick_product == 0:
            break
        elif pick_product not in select_ids:
            print('Invalid option selected')
        else:
            continue
    return select_product

def delete_from_db(connection):
    select_ids = [id[0] for id in execute_sql_select(connection, 'SELECT order_id FROM Orders')]
    while True:
        id = int(input('Please select an Order to delete! \n'))
        if id in select_ids:
            execute_sql(connection, f'DELETE FROM Basket WHERE order_id = {id}')
            execute_sql(connection, f'DELETE FROM Orders WHERE order_id = {id}')
            break
        elif id not in select_ids:
            print('Option selected is invalid')


def update_fields_in_orders(connection, table, column_name, entry, id):
    if entry == '' :
        pass
    else:
        execute_sql(connection, f'UPDATE {table} SET {column_name} = "{entry}" WHERE order_id = {id}')


def update_order_in_db(connection):
    existing_ids = [id[0] for id in execute_sql_select(connection, f'SELECT order_id from Orders')]
    while True:
        print_orders(connection)
        id = int(input("Please select the order you want to update "))
        if id in existing_ids:
            update_order_name = input("Please enter the new name\nPress enter to continue\n ")
            update_fields_in_orders(connection, 'Orders', 'full_name', update_order_name, id)
            update_order_address = input("Please enter the new delivery address\n Press enter to continue\n ")
            update_fields_in_orders(connection, 'Orders', 'c_address', update_order_address, id)
            update_phone = input("Please enter the updated phone number\nPress enter to continue\n ")
            update_fields_in_orders(connection, 'Orders', 'phone_number', update_phone, id)
            print_database(connection, 'Couriers')
            update_courier = input("Please enter the updated courier from the list above\n")
            update_status = input("Please enter the updated status of the order\n")
            execute_sql(connection, f'DELETE from Basket where order_id = {id}')
            items = add_products_to_order(connection)
            for item in items:
                execute_sql(connection, f"INSERT into Basket (order_id, products_id) VALUES ({id}, {item})")
            break
        elif id == 0:
            return
        else :
            print('Option selected is not valid')

# ============== Join Functions ===========

def join_table_courier(connection):
    cursor = connection.cursor()
    cursor.execute(f"SELECT o.full_name AS 'Customer', o.live_status AS 'Order', c.courier_name AS 'Courier' FROM Orders o JOIN Couriers c ON o.courier = c.couriers_id")
    table = from_db_cursor(cursor)
    print(table)
    cursor.close()


def join_table_orders(connection):
    cursor = connection.cursor()
    cursor.execute(f"SELECT o.full_name AS 'Customer', o.c_address AS 'Delivery Address', GROUP_CONCAT(p.product_name separator', ')  AS 'Items Ordered' FROM Orders o JOIN Basket b ON o.order_id = b.order_id JOIN Products p ON p.products_id = b.products_id GROUP BY o.order_id")
    table = from_db_cursor(cursor)
    print(table)
    cursor.close()