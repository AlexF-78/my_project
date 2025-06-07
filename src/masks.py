def get_mask_card_number(card_number: str) -> str:
    """
    Маскирует номер карты в формате XXXX XX** **** XXXX.
    где X - цифры номера карты
    """
    if len(card_number) != 16:
        raise ValueError('Invalid card number')
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
    if len(account_number) != 10:
        raise ValueError('Invalid account number')

    # Получаем последние 4 цифры
    visible_end = account_number[-4:]

    # Формируем мас
    # кированный номер
    masked_account_number = f"**{visible_end}"

    return masked_account_number
