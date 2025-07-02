# import pytest
from unittest.mock import MagicMock, patch

from src.read_xlsx_csv import read_csv_file, read_xlsx_file


@patch("pandas.read_csv")
def test_read_csv_file_success(mock_read_csv):
    # Создаём фиктивный DataFrame
    mock_df = MagicMock()
    mock_df.to_dict.return_value = [
        {"date": "2023-10-01", "amount": 100, "description": "Grocery"},
        {"date": "2023-10-02", "amount": 50, "description": "Gas"},
    ]
    mock_read_csv.return_value = mock_df

    # Вызов функции
    result = read_csv_file("dummy_path.csv")

    # Проверка вызова pandas.read_csv с правильным аргументом
    mock_read_csv.assert_called_once_with("dummy_path.csv")

    # Проверка результата
    assert isinstance(result, list)
    assert len(result) == 2
    assert result[0]["amount"] == 100


@patch("pandas.read_csv", side_effect=Exception("Ошибка чтения файла"))
def test_read_csv_file_exception(mock_read_csv):
    result = read_csv_file("wrong_path.csv")
    assert result == []


# Тест для функции read_xlsx_file
@patch("pandas.read_excel")
def test_read_xlsx_file_success(mock_read_excel):
    # Создаем фиктивный DataFrame
    mock_df = MagicMock()
    mock_df.to_dict.return_value = [
        {"date": "2023-10-01", "amount": 200, "description": "Salary"},
        {"date": "2023-10-03", "amount": 75, "description": "Freelance"},
    ]
    mock_read_excel.return_value = mock_df

    # Вызов функции
    result = read_xlsx_file("dummy_path.xlsx")

    # Проверка вызова pandas.read_excel с правильным аргументом
    mock_read_excel.assert_called_once_with("dummy_path.xlsx")

    # Проверка результата
    assert isinstance(result, list)
    assert len(result) == 2
    assert result[0]["date"] == "2023-10-01"
    assert result[1]["amount"] == 75


@patch("pandas.read_excel", side_effect=Exception("Ошибка чтения файла"))
def test_read_xlsx_file_exception(mock_read_excel):
    result = read_xlsx_file("wrong_path.xlsx")
    assert result == []
