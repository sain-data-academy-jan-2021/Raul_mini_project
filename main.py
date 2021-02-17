import os
import sys
import csv
import module_menus, module_menu_logic
import pymysql
import os
from dotenv import load_dotenv
from prettytable import from_db_cursor
# git commands # git branch -D main 
load_dotenv()
host = os.environ.get("mysql_hosr")
user = os.environ.get("mysql_user")
password = os.environ.get("mysql_pass")
database = os.environ.get("mysql_db")

def start_program():
    connection = pymysql.connect(
        host,
        user,
        password,
        database
    )
    choice_main_menu = module_menus.main_menu()
    while choice_main_menu != "4":
        if choice_main_menu == "1":
            os.system("clear")
            choice_product_menu = module_menus.product_menu()
            module_menu_logic.product_menu_logic(choice_product_menu, connection)
            os.system("clear")
            choice_main_menu = module_menus.main_menu()
        elif choice_main_menu == "2":
            os.system("clear")
            choice_courier_menu = module_menus.courier_menu()
            module_menu_logic.courier_menu_logic(choice_courier_menu, connection)
            os.system("clear")
            choice_main_menu = module_menus.main_menu()
        elif choice_main_menu == "3":
            os.system("clear")    
            choice_order_menu = module_menus.order_menu()
            module_menu_logic.order_menu_logic(choice_order_menu)
            os.system("clear")
            choice_main_menu = module_menus.main_menu()
        else: 
            os.system("clear")
            print("Option selected is invalid")
            choice_main_menu = module_menus.main_menu()

    print("Goodbye ")
    connection.close()
    sys.exit(0)



start_program()

