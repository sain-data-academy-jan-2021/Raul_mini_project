

def delete_product(connection):
    delete_product = int(input('What product would you like to delete? \n'))
    # try:
    #     for index, item in enumerate(connection):
    #         if delete_product in item.values():
    # except KeyError:
    #     print(f"{delete_product} selected does not exist. Please try again")
    sql = (f'DELETE FROM Products WHERE products_id = "{delete_product}" ')
    execute_sql(connection, sql)
    

@patch("builtins.input")
@patch("module_crud.print_products")
@patch("")
def test_delete_product(