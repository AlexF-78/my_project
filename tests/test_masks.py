import pytest

from src.masks import get_mask_account, get_mask_card_number


# тестирование функции get_mask_card_number с параметризацией
@pytest.mark.parametrize(
    "input_number, expected_output",
    [
        ("1234567890123456", "123456 **** 3456"),
        ("9876543210987654", "987654 **** 7654"),
    ],
)
def test_get_mask_card_number(input_number, expected_output):
    result = get_mask_card_number(input_number)
    assert result == expected_output


# тестирование функции get_mask_account с различными входными данными
@pytest.mark.parametrize(
    "account_number, expected_output",
    [
        ("1234567890", "**7890"),
        ("0987654321", "**4321"),
    ],
)
def test_get_mask_account(account_number, expected_output):
    result = get_mask_account(account_number)
    assert result == expected_output


# Дополнительный тест на  некорректные данные
def test_invalid_input_types():
    with pytest.raises(TypeError):
        get_mask_card_number(1234567890)
