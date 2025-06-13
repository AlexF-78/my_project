def filter_by_currency(transactions, currency_code):
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


def transaction_descriptions(transactions):
    """
    Генератор, который по очереди возвращает описание каждой транзакции из списка.
    """
    for transaction in transactions:
        description = transaction.get('description', '').lower()

        # Варианты описаний
        if 'перевод организации' in description:
            yield 'Перевод организации'
        elif 'перевод со счета на счет' in description:
            yield 'Перевод со счета на счет'
        elif 'перевод с карты на карту' in description:
            yield 'Перевод с карты на карту'
        else:
            # Для любых других случаев
            yield description.capitalize() or 'Описание не указано'
