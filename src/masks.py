from src.logging_config import logging

logger = logging.getLogger('masks')

logger.info("Запуск модуля masks.py")


def get_mask_card_number(card_number: str) -> str:
    """
    Маскирует номер карты в формате XXXX XX** **** XXXX.
    где X - цифры номера карты
    """
    logger.info(f"Начало маскировки номера карты: {card_number}")
    try:
        if len(card_number) != 16:
            raise ValueError("Invalid card number")
        # Первые 6 цифр
        first_numbers = card_number[:6]
        # Последние 4 цифры
        recent_numbers = card_number[-4:]
        # Заменяем остальные цифры на звездочки
        masked_numbers = "****"
        # Формируем маскированный номер
        masked_card_number = f"{first_numbers} {masked_numbers} {recent_numbers}"
        return masked_card_number
    except Exception as e:
        logger.error(f"Ошибка при маскировке номера карты: {e}")
        raise


def get_mask_account(account_number: str) -> str:
    """
    Маскирует номер счета в формате **XXXX.
    где X - цифры номера счета .
    """
    logger.info(f"Начало маскировки номера счета: {account_number}")
    try:
        if len(account_number) != 10:
            raise ValueError("Invalid account number")

        # Получаем последние 4 цифры
        visible_end = account_number[-4:]

        # Формируем маскированный номер
        masked_account_number = f"**{visible_end}"
        logger.info(f"Маскированный номер счета: {masked_account_number}")
        return masked_account_number
    except Exception as e:
        logger.error(f"Ошибка при маскировке номера счёта: {e}")
        raise
