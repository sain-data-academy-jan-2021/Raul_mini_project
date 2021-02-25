import os
import csv
import module_print, module_menus, module_crud
import pandas as pd
import pymysql
from prettytable import from_db_cursor


def product_menu_logic(choice, connection):
    while choice != "0":
        if choice == "1":
            os.system("clear")
            module_crud.print_products(connection)
            choice = module_menus.product_menu()

        elif choice == "2":
            os.system("clear")
            module_crud.add_product(connection)
            while True:
                add_more = input("Do you want to add another one?\n Yes or No \n").title()
                os.system("clear")
                if add_more != "No" :
                    module_crud.add_product(connection)
                else:
                    break
            choice = module_menus.product_menu()

        elif choice == "3":
            os.system("clear")
            module_crud.print_products(connection)
            module_crud.update_product(connection)
            choice = module_menus.product_menu()    

        elif choice == "4":
            os.system("clear")
            module_crud.print_products(connection)
            module_crud.delete_product(connection)
            choice = module_menus.product_menu()

        else:
            os.system("clear")
            print("Option selected is invalid")
            choice = module_menus.product_menu()

def order_menu_logic(choice, connection):
    while choice != "0":
        if choice == "1":
            os.system('clear')
            module_crud.print_orders(connection)
            choice = module_menus.order_menu()

        elif choice == "2":
            os.system("clear")
            module_crud.add_order_to_db(connection)
            choice = module_menus.order_menu()

        elif choice == "3":
            os.system("clear")
            module_crud.update_order_in_db(connection)
            choice = module_menus.order_menu()

        elif choice == "4":
            # Delete product
            os.system("clear")
            module_crud.print_orders(connection)
            module_crud.delete_from_db(connection)
            choice = module_menus.order_menu()       

        else:
            os.system("clear")
            print("Option selected is invalid")
            choice = module_menus.order_menu()


def courier_menu_logic(choice, connection):
    while choice != "0":
        if choice == "1":
            os.system("clear")
            module_crud.print_couriers(connection)
            choice = module_menus.courier_menu()

        elif choice == "2":
            os.system('clear')
            module_crud.add_courier(connection)
            choice = module_menus.courier_menu()

        elif choice == "3":
            os.system("clear")
            module_crud.print_couriers(connection)
            module_crud.update_courier(connection)
            choice = module_menus.courier_menu()

        elif choice == "4":
            os.system("clear")
            module_crud.print_couriers(connection)
            module_crud.delete_courier(connection)
            choice = module_menus.courier_menu()

        else:
            os.system("clear")
            print("Option selected is invalid")
            choice = module_menus.product_menu()

