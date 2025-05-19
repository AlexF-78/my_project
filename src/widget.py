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


