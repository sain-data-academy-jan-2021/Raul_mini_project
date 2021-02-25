def main_menu():
    user_choice =  input(""" 

 _____   __   ___       __ __  
| _ \ \ / /  / __|__ _ / _|\_\ 
|  _/\ V /  | (__/ _` |  _/ -_)
|_|   |_|    \___\__,_|_| \___|
                                   
    ___________________________
    |•1• Enter Products Menu  |
    |•2• Enter Courier Menu   |
    |•3• Enter Orders         |
    |•4• Exit App             |
    ---------------------------
Please Make a Selection
""")
# returns/saves user input to be used later on
    return user_choice

def product_menu(): 
    user_choice = input ("""

 ___ _                  _             ___         _       _   
/ __| |_  ___ _ __ _ __(_)_ _  __ _  | _ )__ _ __| |_____| |_ 
\__ | ' \/ _ | '_ | '_ | | ' \/ _` | | _ / _` (_-| / / -_|  _|
|___|_||_\___| .__| .__|_|_||_\__, | |___\__,_/__|_\_\___|\__|
             |_|  |_|         |___/                            
    _____________________________
    |•1• View Ready Meal-Lunches|
    |•2• Add a Meal to Basket   |
    |•3• Update Meal from Basket|
    |•4• Remove Meal from Basket|
    |•0• Return to Main Menu    |
    -----------------------------
Please Make a Selection
""")
    return user_choice

def courier_menu(): 
    user_choice = input ("""

   ___              _           ___                 _      
 / __|___ _  _ _ _(_)___ _ _  |   \ ___ _ __  __ _(_)_ _  
| (__/ _ | || | '_| / -_| '_| | |) / _ | '  \/ _` | | ' \ 
 \___\___/\_,_|_| |_\___|_|   |___/\___|_|_|_\__,_|_|_||_|
                                                              
    _____________________________
    |•1• View All Couriers      |
    |•2• Add a Courier          |
    |•3• Update a Courier       |
    |•4• Remove a Courier       |
    |•0• Return to Main Menu    |
    -----------------------------
Please Make a Selection
""")
    return user_choice
# takes user input and saves it in a variable

def order_menu():
    user_choice =  input(""" 

  ___         _           __  __              
 / _ \ _ _ __| |___ _ _  |  \/  |___ _ _ _  _ 
| (_) | '_/ _` / -_| '_| | |\/| / -_| ' | || |
 \___/|_| \__,_\___|_|   |_|  |_\___|_||_\_,_|
                                                 
    _____________________
    |•1• View Orders    |
    |•2• Add Order      |
    |•3• Update Status  |
    |•4• Delete Order   |
    |•0• Exit App       |
    ---------------------
Please Make a Selection
""")
    return user_choice
