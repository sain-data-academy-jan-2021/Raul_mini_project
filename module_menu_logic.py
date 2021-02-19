import os
import csv
import module_print, module_menus, module_crud
import pandas as pd
import pymysql
from prettytable import from_db_cursor


# Read data from csv files 
# orders = module_crud.load_data("datastore/order.csv")
# products = module_crud.load_data("datastore/product.csv") 
# couriers = module_crud.load_data("datastore/courier.csv")

# def print_couriers(connection):
#     cursor = connection.cursor()
#     cursor.execute('SELECT couriers_id, name, phone FROM Couriers')
#     mytable = from_db_cursor(cursor)
#     print(mytable)

# def print_products(connection):
#     cursor = connection.cursor()
#     cursor.execute('SELECT products_id, product_name, price FROM Products')
#     mytable = from_db_cursor(cursor)
#     print(mytable)

# def update_product(connection):
#     print_products(connection)
#     product_select = input('What product would you like to update? \n')
#     new_name = input('What would you like to updated to \n Press enter to continue \n')
#     if new_name == '' :
#         pass 
#     else:
#         cursor = connection.cursor()
#         cursor.execute(f'UPDATE Products SET product_name = "{new_name}" WHERE products_id = "{product_select}"')
#     new_price = input('Please enter a price for the product \n Press enter to continue \n')
#     if new_price == '' :
#         pass
#     else:
#         cursor = connection.cursor()
#         cursor.execute(f'UPDATE Products SET price = "{new_price}" WHERE products_id = "{product_select}"')
#     cursor.close()
#     connection.commit()

# def delete_product(connection):
#     print_products()
#     delete_product = input('What product would you like to delete? \n')
#     cursor = connection.cursor()
#     cursor.execute(f'DELETE FROM Products WHERE product_name = "{delete_product}" ')
#     cursor.close()
#     connection.commit()

# def add_product(connection):
#     new_product = input("What product would you like to add? \n").title()
#     while True:
#         try:
#             product_price = float(input("What is the price of the product? \n"))
#             break
#         except ValueError:
#             print('Please enter a number')
#     cursor = connection.cursor()
#     cursor.execute(f'INSERT INTO Products (product_name, price) VALUES ("{new_product}", {product_price})')
#     cursor.close()
#     connection.commit()

def product_menu_logic(choice, connection):
    while choice != "0":
        if choice == "1":
            os.system("clear")
            module_crud.print_products(connection)
            # data = cursor.execute('SELECT products_id, product_name, price FROM Products')
            choice = module_menus.product_menu()
        elif choice == "2":
            # Add new products
            os.system("clear")
            module_crud.add_product(connection)
            # # Ask if user wants to add more products
            add_more = input("Do you want to add another one? Yes or No \n").title()
            os.system("clear")
            if add_more != "No":
                module_crud.add_product(connection)
            choice = module_menus.product_menu()
        elif choice == "3":
            # Update product
            os.system("clear")
            module_crud.print_products(connection)
            module_crud.update_product(connection)
            choice = module_menus.product_menu()    
        elif choice == "4":
            # Delete product
            os.system("clear")
            module_crud.print_products(connection)
            module_crud.delete_product(connection)
            # Print all the products
            # module_print.print_from_file("datastore/product.csv")

            # delete_product = input("Which product would you like to delete? \n").title()
            
            # # Check if the product exists
            # if not any (d['Name'] == delete_product for d in products):
            #     print(f"Product {delete_product} does not exist. Please try again")
            # else:
            #     module_crud.remove_data(products, delete_product, "datastore/product.csv")                


            choice = module_menus.product_menu()
        else:
            os.system("clear")
            print("Option selected is invalid")
            choice = module_menus.product_menu()

def order_menu_logic(choice, connection):
    while choice != "0":
        if choice == "1":
            # Display all orders
            os.system('clear')
            module_crud.print_orders(connection)
            choice = module_menus.order_menu()
        elif choice == "2":
            # Add a new order
            os.system("clear")
            module_crud.add_order_to_db(connection)
            choice = module_menus.order_menu()
        elif choice == "3":
            os.system("clear")
            module_print.print_from_file("datastore/order.csv")

            order_to_update = input("Which order would you like to update? \n").title()

            os.system("clear")

            if not any(d['Name'] == order_to_update for d in orders):
                print(f"Order {order_to_update} does not exist. Please try again")
            else:
                updated_order = input("Please enter the updated status of the order \n").title()
                module_crud.update_order_status(order_to_update, updated_order, orders)    
            choice = module_menus.order_menu()
        elif choice == "4":
            # Delete product
            os.system("clear")
            # Print all the orders
            module_print.print_from_file("datastore/order.csv")
            # select key to delete from dictionary, use title for capitalize input
            select_order = input("Please select a order to delete \n")
            
            # Check if exists
            if not any (d['Name'] == select_order for d in orders):
                print(f"Order {select_order} does not exist. Please try again")
            else:
                module_crud.remove_data(orders, select_order, "datastore/order.csv")    

            choice = module_menus.order_menu()       
        else:
            os.system("clear")
            print("Option selected is invalid")
            choice = module_menus.order_menu()


def courier_menu_logic(choice, connection):
    # Courier
    while choice != "0":
        if choice == "1":
            os.system("clear")
            # Print all the couriers
            module_crud.print_couriers(connection)
            choice = module_menus.courier_menu()

        elif choice == "2":
            # Add courier
            os.system('clear')
            module_crud.add_courier(connection)
            choice = module_menus.courier_menu()

        elif choice == "3":
            # Update courier
            os.system("clear")
            module_crud.print_couriers(connection)
            module_crud.update_courier(connection)
            choice = module_menus.courier_menu()

        elif choice == "4":
            # Delete courier
            os.system("clear")
            module_crud.print_couriers(connection)
            module_crud.delete_courier(connection)
            choice = module_menus.courier_menu()

        else:
            os.system("clear")
            print("Option selected is invalid")
            choice = module_menus.product_menu()

