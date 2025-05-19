from datetime import datetime
from .masks import get_mask_card_number, get_mask_account


def mask_account_card(info: str) -> str:
    """
    Функция маскировки информации карты или счета
    """
    parts = info.split()
    if not parts:
        return info

    # определяем тип по первому слову
    first_word = parts[0]
    if first_word.lower() == "счет":
        # Обработка счета
        score_number = parts[1]
        masked = get_mask_account(score_number)
        return f"Счет {masked}"
    else:
        digit_card = parts[-1]
        card_type = " ".join(parts[:-1])
        masked_number = get_mask_card_number(digit_card)
        return f"{card_type} {masked_number}"


def get_date(date_str: str) -> str:
    """Форматирует дату"""
    dt = datetime.fromisoformat(date_str)
    return dt.strftime("%d.%m.%Y")

print(mask_account_card("Visa Platinum 7000792289606361"))
# Вывод: Visa Platinum 7000 79** **** 6361

print(mask_account_card("Счет 73654108430135874305"))
# Вывод: Счет **4305

print(get_date("2024-03-11T02:26:18.671407"))
# Вывод: 11.03.2024
