def get_mask_card_number(card_number: str) -> str:
    """
    Маскирует номер карты в формате XXXX XX** **** XXXX.
    где X - цифры номера карты
    """
    if card_number is None:
        return None
    if not isinstance(card_number, str):
        raise TypeError("Card number must be a string")
    length = len(card_number)
    if length <= 4:
        return card_number
    elif length <= 15:
        return card_number
    else:
        return card_number[:6] + " **** " + card_number[-4:]

    # Первые 6 цифр
    first_numbers = card_number[:6]
    # Последние 4 цифры
    recent_numbers = card_number[-4:]

    # Заменяем остальные цифры на звездочки
    masked_numbers = "****"

    # Формируем маскированный номер
    masked_card_number = f"{first_numbers} {masked_numbers} {recent_numbers}"

    return masked_card_number


def get_mask_account(account_number: str) -> str:
    """
    Маскирует номер счета в формате **XXXX.
    где X - цифры номера счета .

    """

    if account_number is None:
        return None
    if not isinstance(account_number, str):
        raise TypeError("Account number must be a string")
    if len(account_number) <= 4:
        return account_number

    # Получаем последние 4 цифры
    visible_end = account_number[-4:]

    # Формируем мас
    # кированный номер
    masked_account_number = f"**{visible_end}"

    return masked_account_number
