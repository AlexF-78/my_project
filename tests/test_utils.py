import json
import unittest
from unittest.mock import mock_open, patch

from src.utils import read_json_file


class TestReadJsonFile(unittest.TestCase):

    @patch("os.path.exists")
    @patch("builtins.open", new_callable=mock_open)
    def test_file_not_exists(self, mock_open_fn, mock_exists):
        # Файл не существует
        mock_exists.return_value = False
        result = read_json_file("some_path.json")
        self.assertEqual(result, [])
        mock_open_fn.assert_not_called()

    @patch("os.path.exists")
    @patch("builtins.open", new_callable=mock_open)
    def test_empty_json(self, mock_open_fn, mock_exists):
        # Файл существует и содержит пустой JSON-массив
        mock_exists.return_value = True
        mock_open_fn.return_value.read.return_value = "[]"
        # Передаем JSON-строку в open
        with patch("json.load", return_value=[]):
            result = read_json_file("some_path.json")
            self.assertEqual(result, [])

    @patch("os.path.exists")
    @patch("builtins.open", new_callable=mock_open)
    def test_invalid_json(self, mock_open_fn, mock_exists):
        # Файл содержит некорректный JSON
        mock_exists.return_value = True
        mock_open_fn.return_value.read.return_value = "{ invalid json }"
        # Вызов json.load вызовет исключение JSONDecodeError
        with patch("json.load", side_effect=json.JSONDecodeError("error", "doc", 0)):
            result = read_json_file("some_path.json")
            self.assertEqual(result, [])

    @patch("os.path.exists")
    @patch("builtins.open", new_callable=mock_open)
    def test_json_not_list(self, mock_open_fn, mock_exists):
        # Файл содержит JSON-объект вместо списка
        mock_exists.return_value = True
        mock_open_fn.return_value.read.return_value = '{"key": "value"}'
        with patch("json.load", return_value={"key": "value"}):
            result = read_json_file("some_path.json")
            self.assertEqual(result, [])

    @patch("os.path.exists")
    @patch("builtins.open", new_callable=mock_open)
    def test_valid_list_json(self, mock_open_fn, mock_exists):
        # Файл содержит корректный список словарей
        data = [{"id": 1}, {"id": 2}]
        mock_exists.return_value = True
        mock_open_fn.return_value.read.return_value = json.dumps(data)
        with patch("json.load", return_value=data):
            result = read_json_file("some_path.json")
            self.assertEqual(result, data)


if __name__ == "__main__":
    unittest.main()
