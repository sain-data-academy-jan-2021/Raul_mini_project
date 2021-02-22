import module_crud
from unittest.mock import patch, Mock



@patch("builtins.input")
@patch("module_crud.execute_sql")
def test_delete_product(mock_execute, mock_input):
    # Assemble
    mock_input.side_effect = ['2', 'Latte', 1.9]
    expected_sql = (f'DELETE FROM Products WHERE products_id = "2"')
    # Act
    module_crud.delete_product(None)
    # Assert
    mock_execute.assert_called_with(None, expected_sql)
    print('Test has passed')
test_delete_product()