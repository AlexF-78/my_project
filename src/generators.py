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
