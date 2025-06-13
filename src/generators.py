# transactions = [
#     {
#         "id": 939719570,
#         "state": "EXECUTED",
#         "date": "2018-06-30T02:08:58.425572",
#         "operationAmount": {
#             "amount": "9824.07",
#             "currency": {
#                 "name": "USD",
#                 "code": "USD"
#             }
#         },
#         "description": "Перевод организации",
#         "from": "Счет 75106830613657916952",
#         "to": "Счет 11776614605963066702"
#     },
#     {
#         "id": 142264268,
#         "state": "EXECUTED",
#         "date": "2019-04-04T23:20:05.206878",
#         "operationAmount": {
#             "amount": "79114.93",
#             "currency": {
#                 "name": "USD",
#                 "code": "USD"
#             }
#         },
#         "description": "Перевод со счета на счет",
#         "from": "Счет 19708645243227258542",
#         "to": "Счет 75651667383060284188"
#     },
#     {
#         # Транзакция с другой валютой для примера
#         "id": 123456789,
#         "state": "EXECUTED",
#         "date": "2020-01-01T10:00:00.000000",
#         "operationAmount": {
#             "amount": "1000.00",
#             # Валюта не USD
#             # или другой код валюты
#             # например, EUR
#             # чтобы проверить фильтр по другим валютам
#             # можно добавить такие случаи
#             # В этом примере пропустим их для простоты.
#         },
#         # остальные поля...
#     }
# ]
#


def filter_by_currency(transactions, currency_code):
    for transaction in transactions:
        # Проверяем, что у транзакции есть нужные данные
        operation_amount = transaction.get('operationAmount')
        if not operation_amount:
            # пропускаем, если нет 'operationAmount'
            continue

        currency_info = operation_amount.get('currency')
        if not currency_info:
            # пропускаем, если нет 'currency'
            continue

        code = currency_info.get('code')
        if not code:
            # пропускаем, если нет 'code'
            continue

        if code == currency_code:
            yield transaction

# usd_transactions = filter_by_currency(transactions, "USD")
# for _ in range(2):
#     print(next(usd_transactions))
