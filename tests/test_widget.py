import pytest

from src.widget import get_date, mask_account_card


# Моки для функций маскировки
def mock_get_mask_card_number(card_number):
    return f"****{card_number[-4:]}"


def mock_get_mask_account(account_number):
    return f"****{account_number[-4:]}"


# Фикстуры для маскировки
@pytest.fixture(autouse=True)
def patch_masks(monkeypatch):
    monkeypatch.setattr("src.widget.get_mask_card_number", mock_get_mask_card_number)
    monkeypatch.setattr("src.widget.get_mask_account", mock_get_mask_account)


# Тесты для mask_account_card
@pytest.mark.parametrize(
    "input_str, expected_output",
    [
        ("счёт 1234561234567890", "Счет ****7890"),
        ("Visa Classic 1234", "Visa Classic ****1234"),
        ("Счет 1234561234567890", "Счет ****7890"),
        ("Visa Classic 1234567890123456", "Visa Classic ****3456"),
        ("MasterCard Gold 9876543210987654", "MasterCard Gold ****7654"),
    ],
)
def test_mask_account_card_correct(input_str, expected_output):
    result = mask_account_card(input_str)
    assert result == expected_output


# Тест на некорректный ввод (пустая строка)
def test_mask_account_card_empty():
    assert mask_account_card("") == ""


# Тест на случай, когда нет номера карты или счета
def test_mask_account_card_missing_parts():
    # Вход без номера счета/карты
    with pytest.raises(ValueError):
        mask_account_card("Счет")
    with pytest.raises(ValueError):
        mask_account_card("Visa")


# Тестирование get_date с валидными датами
@pytest.mark.parametrize(
    "input_str, expected_date",
    [
        ("2023-10-05T14:30:00", "05.10.2023"),
        ("2000-01-01T00:00:00", "01.01.2000"),
    ],
)
def test_get_date_valid(input_str, expected_date):
    assert get_date(input_str) == expected_date


# Тестирование get_date с некорректным форматом
def test_get_date_invalid():
    with pytest.raises(ValueError):
        get_date("not-a-date")


# Тестирование get_date с пустой строкой
def test_get_date_empty():
    with pytest.raises(ValueError):
        get_date("")


# Граничные случаи: очень короткая строка или неправильный формат
@pytest.mark.parametrize(
    "input_str",
    [
        "2023-13-01T00:00:00",  # неправильный месяц
        "2023-02-30T00:00:00",  # неправильная дата
    ],
)
def test_get_date_edge_cases(input_str):
    with pytest.raises(ValueError):
        get_date(input_str)
