import unittest
from unittest.mock import patch
from homework1 import check_conditions, convert_bushels_to_pounds

class TestHomework1(unittest.TestCase):

    @patch('builtins.input', side_effect=['35', '7'])
    def test_check_conditions_optimal(self, mock_input):
        with patch('builtins.print') as mock_print:
            check_conditions()
            mock_print.assert_called_once_with("These conditions are optimal for growing corn.")

    @patch('builtins.input', side_effect=['25', '5'])
    def test_check_conditions_not_optimal(self, mock_input):
        with patch('builtins.print') as mock_print:
            check_conditions()
            mock_print.assert_called_once_with("These conditions are not optimal for growing corn.")

    @patch('builtins.input', return_value='10')
    def test_convert_bushels_to_pounds(self, mock_input):
        with patch('builtins.print') as mock_print:
            convert_bushels_to_pounds()
            mock_print.assert_called_once_with("10.0 bushels of wheat is approximately 600.0 pounds.")

if __name__ == '__main__':
    unittest.main()