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
    

@patch("builtins.input")
@patch("module_crud.print_products")
@patch("")
def test_update_product(