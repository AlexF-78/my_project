# import pytest

from src.bank_processing import process_bank_operations

# Тестовые данные
TEST_DATA = [
    {"description": "Перевод организации", "amount": "1000"},
    {"description": "Перевод с карты на карту", "amount": "500"},
    {"description": "Оплата услуг", "amount": "200"},
    {"description": "Покупка в магазине", "amount": "300"},
    {"description": "Перевод организации", "amount": "400"},
    {"description": "Оплата услуг", "amount": "150"},
    {"description": "Снятие наличных", "amount": "50"},
]


def test_basic_functionality():
    categories = ["Перевод организации", "Оплата услуг"]
    result = process_bank_operations(TEST_DATA, categories)
    assert result == {"Перевод организации": 2, "Оплата услуг": 2}


def test_case_insensitivity():
    categories = ["перевод", "оплата"]
    result = process_bank_operations(TEST_DATA, categories)
    assert result == {"перевод": 3, "оплата": 2}


def test_empty_input():
    assert process_bank_operations([], ["категория"]) == {}
    assert process_bank_operations(TEST_DATA, []) == {}
    assert process_bank_operations([], []) == {}


def test_no_matches():
    result = process_bank_operations(TEST_DATA, ["Несуществующая категория"])
    assert result == {"Несуществующая категория": 0}


def test_partial_matches():
    result = process_bank_operations(TEST_DATA, ["Перевод", "Оплата"])
    assert result == {"Перевод": 3, "Оплата": 2}


def test_multiple_word_categories():
    result = process_bank_operations(TEST_DATA, ["Перевод организации"])
    assert result == {"Перевод организации": 2}
