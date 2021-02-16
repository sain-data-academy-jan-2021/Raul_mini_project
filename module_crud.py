import csv
from os import write
import module_print

# Field names for their respective files
order_field_names = ['Name', 'Address', 'Phone', 'Courier', 'Status', 'Items']
courier_field_names = ['Name', 'Phone']
product_field_names = ['Name', 'Price']

""" 
----- CRUD - Create, Read, Update, Delete -----

"""

# --- Create ---
def save_data(data, file):
    # Access the csv file
    with open(file, 'w') as datafile:
        # Check which file
        if file == 'datastore/order.csv':
            writer = csv.DictWriter(datafile, fieldnames=order_field_names)
            writer.writeheader()
            writer.writerows(data)
        elif file == 'datastore/courier.csv':
                writer = csv.DictWriter(datafile, fieldnames=courier_field_names)
                writer.writeheader()
                writer.writerows(data)
        elif file == 'datastore/product.csv':
                writer = csv.DictWriter(datafile, fieldnames=product_field_names)
                writer.writeheader()
                writer.writerows(data)   

# --- Read ---
def load_data(file):
    tmpData = []
    reader = csv.DictReader(open(file))
    for row in reader:
        tmpData.append(row)
    return tmpData    

# --- Update ---
def update_product(name, price, data):
    for dicts in data:
        if dicts['Name'] == name:
            dicts['Price'] = price
    save_data(data, "datastore/product.csv")


def update_courier(name, phone, data):
    for dicts in data:
        if dicts['Name'] == name:
            dicts['Phone'] = phone
    save_data(data, "datastore/courier.csv")        

# Name,Address,Phone,Courier,Status,Items

def update_order_status(name, status, data):
    for dicts in data:
        if dicts['Name'] == name:
            dicts['Status'] = status
    save_data(data, "datastore/order.csv")        

# --- Delete ---
def remove_data(data, delete_data, file):
    try:
        for index, item in enumerate(data):
            if delete_data in item.values():
                del data[index]
        save_data(data, file)
        print(f"{delete_data} has been removed successfully. Changes are shown below")
        module_print.print_from_file(file)
    except KeyError:
        print(f"{delete_data} selected does not exist. Please try again")    



