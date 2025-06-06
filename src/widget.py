from datetime import datetime

from .masks import get_mask_account, get_mask_card_number


def mask_account_card(info: str) -> str:
    """
    Маскирует информацию о счёте или карте.
    """
    parts = info.split()
    if not parts:
        return info
    first_word = parts[0]
    if first_word.lower() == "счет":
        if len(parts) != 16:
            raise ValueError('Invalid parts number')
        score_number = parts[1]
        masked = get_mask_account(score_number)
        return f"Счет {masked}"
    else:
        if len(parts) < 2:
            return info  # Нет номера карты
        digit_card = parts[-1]
        card_type = " ".join(parts[:-1])
        masked_number = get_mask_card_number(digit_card)
        return f"{card_type} {masked_number}"


def get_date(date_str: str) -> str:
    """Форматирует дату из ISO-формата в дд.мм.гггг."""
    try:
        dt = datetime.fromisoformat(date_str)
        return dt.strftime("%d.%m.%Y")
    except ValueError:
        raise ValueError('Invalid data')
