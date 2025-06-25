import unittest
from unittest.mock import Mock, patch

from src.external_api import convert_currency  # замените на актуальный путь к вашей функции


class TestCurrencyConversion(unittest.TestCase):

    @patch('src.external_api.requests.get')  # замените 'your_module' на название файла, где определена функция
    def test_convert_currency_success(self, mock_get):
        # Мокаем успешный ответ API
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {'result': 123.45}
        mock_get.return_value = mock_response

        result = convert_currency(100, 'USD', 'RUB')
        self.assertEqual(result, 123.45)
        mock_get.assert_called_once()

    @patch('src.external_api.requests.get')
    def test_convert_currency_failure_status(self, mock_get):
        # Мокаем ошибочный статус ответа
        mock_response = Mock()
        mock_response.status_code = 500
        mock_get.return_value = mock_response

        result = convert_currency(100, 'USD', 'RUB')
        self.assertIsNone(result)

    @patch('src.external_api.requests.get')
    def test_convert_currency_no_result_field(self, mock_get):
        # Мокаем ответ без поля 'result'
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {}
        mock_get.return_value = mock_response

        result = convert_currency(100, 'USD', 'RUB')
        self.assertIsNone(result)


if __name__ == '__main__':
    unittest.main()
