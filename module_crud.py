import csv
from os import write
import module_print
import pymysql
from prettytable import from_db_cursor

# Field names for their respective files
# order_field_names = ['Name', 'Address', 'Phone', 'Courier', 'Status', 'Items']
# courier_field_names = ['Name', 'Phone']
# product_field_names = ['Name', 'Price']

# """ 
# ----- CRUD - Create, Read, Update, Delete -----

# """

# # --- Create ---
# def save_data(data, file):
#     # Access the csv file
#     with open(file, 'w') as datafile:
#         # Check which file
#         if file == 'datastore/order.csv':
#             writer = csv.DictWriter(datafile, fieldnames=order_field_names)
#             writer.writeheader()
#             writer.writerows(data)
#         elif file == 'datastore/courier.csv':
#                 writer = csv.DictWriter(datafile, fieldnames=courier_field_names)
#                 writer.writeheader()
#                 writer.writerows(data)
#         elif file == 'datastore/product.csv':
#                 writer = csv.DictWriter(datafile, fieldnames=product_field_names)
#                 writer.writeheader()
#                 writer.writerows(data)   

# # --- Read ---
# def load_data(file):
#     tmpData = []
#     reader = csv.DictReader(open(file))
#     for row in reader:
#         tmpData.append(row)
#     return tmpData    

# # --- Update ---
# def update_product(name, price, data):
#     for dicts in data:
#         if dicts['Name'] == name:
#             dicts['Price'] = price
#     save_data(data, "datastore/product.csv")


# def update_courier(name, phone, data):
#     for dicts in data:
#         if dicts['Name'] == name:
#             dicts['Phone'] = phone
#     save_data(data, "datastore/courier.csv")        

# # Name,Address,Phone,Courier,Status,Items

# def update_order_status(name, status, data):
#     for dicts in data:
#         if dicts['Name'] == name:
#             dicts['Status'] = status
#     save_data(data, "datastore/order.csv")        

# # --- Delete ---
# def remove_data(data, delete_data, file):
#     try:
#         for index, item in enumerate(data):
#             if delete_data in item.values():
#                 del data[index]
#         save_data(data, file)
#         print(f"{delete_data} has been removed successfully. Changes are shown below")
#         module_print.print_from_file(file)
#     except KeyError:
#         print(f"{delete_data} selected does not exist. Please try again")    

# --- DATABASES CRUD MODULES --- 
# --- Products functions ---

def print_products(connection):
    cursor = connection.cursor()
    cursor.execute('SELECT products_id, product_name, price FROM Products')
    mytable = from_db_cursor(cursor)
    print(mytable)

def update_product(connection):
    print_products(connection)
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
    print_products()
    delete_product = input('What product would you like to delete? \n')
    cursor = connection.cursor()
    cursor.execute(f'DELETE FROM Products WHERE product_name = "{delete_product}" ')
    cursor.close()
    connection.commit()

def add_product(connection):
    new_product = input("What product would you like to add? \n").title()
    while True:
        try:
            product_price = float(input("What is the price of the product? \n"))
            break
        except ValueError:
            print('Please enter a number')
    cursor = connection.cursor()
    cursor.execute(f'INSERT INTO Products (product_name, price) VALUES ("{new_product}", {product_price})')
    cursor.close()
    connection.commit()
    
# ---- Couriers Functions ----
def print_couriers(connection):
    cursor = connection.cursor()
    cursor.execute('SELECT couriers_id, name, phone FROM Couriers')
    mytable = from_db_cursor(cursor)
    print(mytable)
    

def update_courier(connection):
    print_couriers(connection)
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
    new_courier = input("What courier would you like to add? \n").title()
    while True:
        try:
            # take the valuea and see if it meets the pattern values ether numeral or spaces, is it between len less than 12
            courier_phone = int(input("What is the phone number of the courier? \n"))
            break
        except ValueError:
            print('Please enter a phone number')
    cursor = connection.cursor()
    cursor.execute(f'INSERT INTO Couriers (courier_name, phone) VALUES ("{new_courier}", "{courier_phone}")')
    cursor.close()
    connection.commit()

