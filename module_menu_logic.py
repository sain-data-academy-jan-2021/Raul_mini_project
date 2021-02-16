import os
import csv
import module_print, module_menus, module_crud
import pandas as pd
import pymysql
import os
from prettytable import from_db_cursor
# made changes to git so that everything workes

# Read data from csv files 
orders = module_crud.load_data("datastore/order.csv")
# products = module_crud.load_data("datastore/product.csv") 
# couriers = module_crud.load_data("datastore/courier.csv")

def print_couriers(connection):
    cursor = connection.cursor()
    cursor.execute('SELECT couriers_id, name, phone FROM Couriers')
    mytable = from_db_cursor(cursor)
    print(mytable)

def print_products(connection):
    cursor = connection.cursor()
    cursor.execute('SELECT products_id, product_name, price FROM Products')
    mytable = from_db_cursor(cursor)
    print(mytable)

def update_product(connection):
    print_products()
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

def product_menu_logic(choice, connection):
    while choice != "0":
        if choice == "1":
            os.system("clear")
            print_products(connection)
            # A cursor is an object that represents a DB cursor,
            # which is used to manage the context of a fetch operation.
            # cursor = connection.cursor()
            # cursor.execute('SELECT product_name, price FROM Products')
            # # Gets all rows from the result
            # rows = cursor.fetchall()
            # for row in rows:
            #     print(f'Products available  {str(row[0])} Price is  {row[1]}')            
            # cursor.close()
            # module_print.print_from_file("datastore/product.csv")
            choice = module_menus.product_menu()
        elif choice == "2":
            # Add new products
            os.system("clear")
            
            add_product(connection)
            
            # # Ask if user wants to add more products
            # add_more = input("Do you want to add another one? Yes or No \n").title()
            # os.system("clear")
            # if add_more != "No":
            #     add_product()
            choice = module_menus.product_menu()
        elif choice == "3":
            # Update product
            os.system("clear")
            update_product(connection)
            # Print all the products
            # module_print.print_from_file("datastore/product.csv")
            # # Ask user for the product to update
            # update_product = input("What proudct would you like to update? \n").title()
            # os.system("clear")
            # if not any(d['Name'] == update_product for d in products):
            #     print(f"Product {update_product} does not exist. Please try again")
            # else:
            #     # Need to work on this
            #     new_price = input("Enter the updated price \n").title()
            #     module_crud.update_product(update_product, new_price, products)
            
            choice = module_menus.product_menu()    
        elif choice == "4":
            # Delete product
            os.system("clear")  
            delete_product(connection)
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

def order_menu_logic(choice):
    while choice != "0":
        if choice == "1":
            # Display all orders
            module_print.print_from_file("datastore/order.csv")
            choice = module_menus.order_menu()
        elif choice == "2":
            # Add a new order
            os.system("clear")
            # Get all the inputs
            name = input("Please enter the name of new order \n").title()
            address = input("Please type the address for delivery \n").title()
            phone = input("Please enter phone number \n").title()
            delv_method = input("Please add the delivery method \n").title()
            status = input("Please enter the status of the order \n").title()
            
            product_choice_input = ""
            # List for all the items user selected
            product_selection = []
            while product_choice_input != "0":
                # prints all the items
                module_print.print_from_file("datastore/product.csv")
                # takes the input
                product_choice_input = input("Select product from list below or type 0 to return \n").title()

                if product_choice_input != "0":
                    # add the user input to the list of items as long as it's not zero
                    product_selection.append(product_choice_input)

            orders.append(
                {'Name': name, 'Address': address, 'Phone': phone, 'Courier': delv_method, 'Status': status,
                 'Items': ','.join(product_selection)}
            )
            module_crud.save_data(orders, "datastore/order.csv")
            module_print.print_from_file("datastore/order.csv")
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
            print_couriers(connection)
            # module_print.print_from_file("courier.csv")
            # loopet backed at line 61 after we done everything in the if block
            choice = module_menus.courier_menu()

        elif choice == "2":
            # Add courier
            os.system("clear")
            new_courier = input("What name would you like to add? \n").title()
            courier_phone = input("What is the phone number? \n").title()
            couriers.append(
                {'Name': new_courier, 'Phone': courier_phone}
            )
            module_crud.save_data(couriers, "courier.csv")

            choice = module_menus.courier_menu()

        elif choice == "3":
            # Update courier
            os.system("clear")
            module_print.print_from_file("courier.csv")

            courier_to_update = input("What courier would you like to update? \n").title()

            os.system("clear")

            if not any(d['Name'] == courier_to_update for d in couriers):
                print(f"Courier {courier_to_update} does not exist. Please try again")
            else:
                updated_courier = input("What would you like to update this to? \n").title()
                module_crud.update_courier(courier_to_update, updated_courier, couriers)
            
            choice = module_menus.courier_menu()

        elif choice == "4":
            # Delete courier
            os.system("clear")
            
            courier_to_delete = input("Which courier would you like to delete? \n").title()

            # Check if it exits 
            if not any(d['Name'] == courier_to_delete for d in couriers):
                print(f"Courier {courier_to_delete} does not exist. Please try again.")
            else:
                module_crud.remove_data(couriers, courier_to_delete, "courier.csv")

            choice = module_menus.courier_menu()

        else:
            os.system("clear")
            print("Option selected is invalid")
            choice = module_menus.product_menu()

