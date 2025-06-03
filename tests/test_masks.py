import pytest
from my_project.src.masks import get_mask_card_number, get_mask_account


# тестирование функции get_mask_card_number с параметризацией
@pytest.mark.parametrize("input_number, expected_output", [
    ("1234567890123456", "123456 **** 3456"),
    ("9876543210987654", "987654 **** 7654"),
    ("1234", "1234"),
    ("12345", "12345"),
    ("", ""),
    (None, None),
    ("12345678901234567890", "123456 **** 7890")
])
def test_get_mask_card_number(input_number, expected_output):
    result = get_mask_card_number(input_number)
    assert result == expected_output

# тестирование функции get_mask_account с различными входными данными
@pytest.mark.parametrize("account_number, expected_output", [
    ("1234567890", "**7890"),
    ("0987654321", "**4321"),
    # короткий номер не маскируется
    ("1234", "1234"),
    # длина > 4, маскируется
    ("56789", "**6789"),
    # пустая строка
    ("", ""),
    # None
    (None, None),
])


def test_get_mask_account(account_number, expected_output):
    result = get_mask_account(account_number)
    assert result == expected_output


# Дополнительный тест на  некорректные данные
def test_invalid_input_types():
    with pytest.raises(TypeError):
        get_mask_card_number(1234567890)