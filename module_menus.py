def main_menu():
    user_choice =  input(""" 



 _____                                           _                   
(____ \       _              /\                 | |                  
 _   \ \ ____| |_  ____     /  \   ____ ____  _ | | ____ ____  _   _ 
| |   | / _  |  _)/ _  |   / /\ \ / ___) _  |/ || |/ _  )    \| | | |
| |__/ ( ( | | |_( ( | |  | |__| ( (__( ( | ( (_| ( (/ /| | | | |_| |
|_____/ \_||_|\___)_||_|  |______|\____)_||_|\____|\____)_|_|_|\__  |
                                                              (____/ 

        ___________________________
        |•1• Enter Products Menu  |
        |•2• Enter Courier Menu   |
        |•3• Enter Orders         |
        |•4• Join Tables          |
        |•5• Exit App             |
        ---------------------------
        Please Make a Selection
""")
# returns/saves user input to be used later on
    return user_choice

def product_menu(): 
    user_choice = input ("""


  ____                _            _         __  __                  
 |  _ \ _ __ ___   __| |_   _  ___| |_ ___  |  \/  | ___ _ __  _   _ 
 | |_) | '__/ _ \ / _` | | | |/ __| __/ __| | |\/| |/ _ \ '_ \| | | |
 |  __/| | | (_) | (_| | |_| | (__| |_\__ \ | |  | |  __/ | | | |_| |
 |_|   |_|  \___/ \__,_|\__,_|\___|\__|___/ |_|  |_|\___|_| |_|\__,_|                                                                    
                          
        _____________________________
        |•1• View all Products      |
        |•2• Add a new Product      |
        |•3• Update a Product       |
        |•4• Remove a Product       |
        |•0• Return to Main Menu    |
        -----------------------------
        Please Make a Selection
""")
    return user_choice

def courier_menu(): 
    user_choice = input ("""


   ____                 _             __  __                  
  / ___|___  _   _ _ __(_) ___ _ __  |  \/  | ___ _ __  _   _ 
 | |   / _ \| | | | '__| |/ _ \ '__| | |\/| |/ _ \ '_ \| | | |
 | |__| (_) | |_| | |  | |  __/ |    | |  | |  __/ | | | |_| |
  \____\___/ \__,_|_|  |_|\___|_|    |_|  |_|\___|_| |_|\__,_|                                                                                          

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

 
   ___          _             __  __                  
  / _ \ _ __ __| | ___ _ __  |  \/  | ___ _ __  _   _ 
 | | | | '__/ _` |/ _ \ '__| | |\/| |/ _ \ '_ \| | | |
 | |_| | | | (_| |  __/ |    | |  | |  __/ | | | |_| |
  \___/|_|  \__,_|\___|_|    |_|  |_|\___|_| |_|\__,_|                                                                                                       
    
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

def joins_menu():
    user_choice =  input(""" 


   _____     _          _______      _     _            
  (_____)   (_)        (_______)    | |   | |           
     _  ___  _ ____     _       ____| | _ | | ____  ___ 
    | |/ _ \| |  _ \   | |     / _  | || \| |/ _  )/___)
 ___| | |_| | | | | |  | |____( ( | | |_) ) ( (/ /|___ |
(____/ \___/|_|_| |_|   \______)_||_|____/|_|\____|___/ 
                                                        


        ______________________________
        |•1• View Customer and Courier|
        |•2• View Customer and Order  |
        |•0• Previous Menu            |
        ------------------------------
        Please Make a Selection
""")
    return user_choice
