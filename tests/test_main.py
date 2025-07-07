# import pytest
import os
import sys
from unittest.mock import patch

from main import main

# Добавляем путь к проекту в PYTHONPATH
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Тестовые данные
TEST_DATA = [
    {
        "state": "EXECUTED",
        "date": "2023-09-05T11:30:32Z",
        "description": "Перевод организации",
        "amount": "16210",
        "currency": "RUB",
        "from": "Счет 58803664561298323391",
        "to": "Счет 39745660563456619397",
    },
    {
        "status": "CANCELED",
        "date": "2023-08-15T14:25:18Z",
        "description": "Оплата услуг",
        "amount": "5000",
        "currency": "USD",
    },
    {
        "state": "PENDING",
        "date": "2023-10-10T09:15:00Z",
        "description": "Покупка в магазине",
        "amount": "1200",
        "currency": "EUR",
    },
]


# Тесты для отдельных функций остаются без изменений
# ...


@patch("builtins.input", side_effect=["3", "executed", "нет", "нет", "нет"])
@patch("main.print_operations")
@patch("main.filter_by_status", return_value=TEST_DATA)
@patch("main.sort_operations", return_value=TEST_DATA)
@patch("main.filter_by_currency", return_value=TEST_DATA)
@patch("main.process_bank_search", return_value=TEST_DATA)
@patch("main.json_transactions", TEST_DATA)
@patch("main.csv_transactions", TEST_DATA)
@patch("main.xlsx_transactions", TEST_DATA)
def test_main_flow(mock_search, mock_currency, mock_sort, mock_filter, mock_print, mock_input):
    """Тестирование основного потока выполнения"""
    main()

    # Проверка вызовов
    mock_filter.assert_called_once_with(TEST_DATA, "executed")
    mock_sort.assert_not_called()
    mock_currency.assert_not_called()
    mock_print.assert_called_once_with(TEST_DATA)


@patch("builtins.input", return_value="1")
@patch("main.json_transactions", [])
def test_main_with_empty_data(mock_input, capsys):
    """Тестирование обработки пустых данных"""
    main()
    captured = capsys.readouterr()
    assert "Не удалось загрузить данные" in captured.out
