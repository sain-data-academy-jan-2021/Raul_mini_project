import module_crud
from unittest.mock import patch, Mock
import unittest
from prettytable import from_db_cursor




class TestApp(unittest.TestCase):
    @patch("builtins.input")
    @patch("module_crud.execute_sql")
    def test_delete_product(self, mock_execute, mock_input):
        # Assemble
        mock_input.side_effect = ['2', 'Latte', 1.9]
        expected_sql = (f'DELETE FROM Products WHERE products_id = "2"')
        # Act
        module_crud.delete_product(None)
        # Assert
        mock_execute.assert_called_with(None, expected_sql)

    @patch("builtins.input")
    @patch("module_crud.execute_sql")
    def test_add_product(self, mock_execute, mock_input):
        # Assemble
        mock_input.side_effect = ['Water', 2.3]
        expected_sql = (f'INSERT INTO Products (product_name, price) VALUES ("Water", 2.3)')
        # Act
        module_crud.add_product(None)
        # Assert
        mock_execute.assert_called_with(None, expected_sql)

    @patch("builtins.input")
    @patch("module_crud.execute_sql")
    def test_delete_courier(self, mock_execute, mock_input):
        # Assemble
        mock_input.side_effect = ['1', 'Andrew', '1234567']
        expected_sql = (f'DELETE FROM Couriers WHERE couriers_id = "1"')
        # Act
        module_crud.delete_courier(None)
        # Assert
        mock_execute.assert_called_with(None, expected_sql)


    @patch("builtins.input")
    @patch("module_crud.execute_sql")
    def test_add_courier(self, mock_execute, mock_input):
        # Assemble
        mock_input.side_effect = ['Alexa', '1234567']
        expected_sql = (f'INSERT INTO Couriers (courier_name, phone) VALUES ("Alexa", "1234567")')
        # Act
        module_crud.add_courier(None)
        # Assert
        mock_execute.assert_called_with(None, expected_sql)
        

    @patch("builtins.input")
    @patch("module_crud.execute_sql")
    def test_update_courier(self, mock_execute, mock_input):
        # Assemble
        mock_input.side_effect = ['4', 'Mike', '01234567']
        expected_sql = (f'UPDATE Couriers SET courier_name = "Mike" WHERE couriers_id = "4"')
        expected_sql = (f'UPDATE Couriers SET phone = "01234567" WHERE couriers_id = "4"')
        # Act
        module_crud.update_courier(None)
        # Assert
        mock_execute.assert_called_with(None, expected_sql)


    @patch("builtins.input")
    @patch("module_crud.execute_sql")
    def test_update_product(self, mock_execute, mock_input):
        # Assemble
        mock_input.side_effect = ['2', 'Water', 2.3]
        expected_sql = (f'UPDATE Products SET product_name = "Water" WHERE products_id = "2"')
        expected_sql = (f'UPDATE Products SET price = 2.3 WHERE products_id = "2"')
        # Act
        module_crud.update_product(None)
        # Assert
        mock_execute.assert_called_with(None, expected_sql)


    # ===== ORDERS =====

    @patch("module_crud.read_orders_db")
    @patch("module_crud.execute_sql_select")
    @patch("builtins.input")
    @patch("module_crud.execute_sql")
    def test_delete_from_db(self, mock_execute_sql, mock_input, mock_execute_select, mock_read_orders_db):
        mock_execute_select.return_value = ((1,), (2,))
        mock_input.return_value = '1'
        expected = 'DELETE FROM Orders WHERE order_id = 1'
        
        module_crud.delete_from_db(None)
        
        mock_execute_sql.assert_called_with(None, expected)
        mock_execute_sql.call_count == 2


if __name__ == '__main__':
    unittest.main()