from typing import Any, Dict, Generator, List


def filter_by_currency(
    transactions: List[Dict[str, Any]],
    currency_code: str
) -> Generator[Dict[str, Any], None, None]:
    """
    Генерирует транзакции из списка, у которых валюта совпадает с заданным кодом.
    """
    for transaction in transactions:
        # Проверяем, что у транзакции есть нужные данные
        operation_amount = transaction.get("operationAmount")
        if not operation_amount:
            # пропускаем, если нет 'operationAmount'
            continue

        currency_info = operation_amount.get("currency")
        if not currency_info:
            # пропускаем, если нет 'currency'
            continue

        code = currency_info.get("code")
        if not code:
            # пропускаем, если нет 'code'
            continue

        if code == currency_code:
            yield transaction


def transaction_descriptions(
    transactions: List[Dict[str, Any]]
) -> Generator[str, None, None]:
    """
    Генератор, который по очереди возвращает описание каждой транзакции из списка.
    """
    for transaction in transactions:
        description = transaction.get("description", "").lower()

        # Варианты описаний
        if "перевод организации" in description:
            yield "Перевод организации"
        elif "перевод со счета на счет" in description:
            yield "Перевод со счета на счет"
        elif "перевод с карты на карту" in description:
            yield "Перевод с карты на карту"
        else:
            # Для любых других случаев
            yield description.capitalize() or "Описание не указано"


def card_number_generator(start: int, end: int) -> Generator[str, None, None]:
    """
    Генератор номеров банковских карт в формате 'XXXX XXXX XXXX XXXX'.
    """
    for number in range(start, end + 1):
        # Форматируем число с ведущими нулями до 16 цифр
        card_number = str(number).zfill(16)
        # Разбиваем на группы по 4 цифры
        formatted_number = " ".join([card_number[i: i + 4] for i in range(0, 16, 4)])
        yield formatted_number
