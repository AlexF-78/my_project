import pytest

from src.bank_operations import process_bank_search

# Тестовые данные
TEST_DATA = [
    {
        'description': 'Перевод организации',
        'amount': '1000',
        'currency': 'RUB'
    },
    {
        'description': 'Перевод с карты на карту',
        'amount': '500',
        'currency': 'USD'
    },
    {
        'description': 'Оплата услуг',
        'amount': '200',
        'currency': 'EUR'
    },
    {
        'description': 'Покупка в магазине',
        'amount': '300',
        'currency': 'RUB'
    },
    {
        'description': None,  # Нет описания
        'amount': '100',
        'currency': 'RUB'
    }
]


@pytest.mark.parametrize("search_term,expected_count", [
    ("перевод", 2),
    ("оплата", 1),
    ("магазин", 1),
    ("несуществующий", 0),
    ("", 0),
])
def test_search_functionality(search_term, expected_count):
    """Тестирование базовой функциональности поиска"""
    result = process_bank_search(TEST_DATA, search_term)
    assert len(result) == expected_count


def test_case_insensitivity():
    """Тестирование регистронезависимого поиска"""
    result_lower = process_bank_search(TEST_DATA, "перевод")
    result_upper = process_bank_search(TEST_DATA, "ПЕРЕВОД")
    assert len(result_lower) == len(result_upper) == 2


def test_special_characters():
    """Тестирование специальных символов в поиске"""
    data = [{'description': 'Payment (special) #123', 'amount': '100'}]
    result = process_bank_search(data, "(special)")
    assert len(result) == 1
    result = process_bank_search(data, "#123")
    assert len(result) == 1


def test_empty_input():
    """Тестирование пустых входных данных"""
    assert process_bank_search([], "test") == []
    assert process_bank_search(TEST_DATA, "") == []
    assert process_bank_search([], "") == []


def test_invalid_regex_chars():
    """Тестирование невалидных regex-символов"""
    data = [{'description': 'Payment [special]', 'amount': '100'}]
    result = process_bank_search(data, "[special]")
    assert len(result) == 1  # Должно работать благодаря re.escape


def test_no_description_field():
    """Тестирование операций без поля description"""
    data = [
        {'amount': '100'},
        {'description': '', 'amount': '200'},
        {'description': 'Valid', 'amount': '300'},
    ]
    result = process_bank_search(data, "valid")
    assert len(result) == 1
