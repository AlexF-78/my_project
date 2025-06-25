import requests

from src.utils import read_json_file

# Путь к файлу с операциями
filepath = "../data/operations.json"
transactions = read_json_file(filepath)

API_KEY = 'LFTn8379Gsgt9PNBCBmho2YiBZ8nGrTE'

# Базовая конечная точка API для конвертации
CONVERT_URL = 'https://api.apilayer.com/exchangerates_data/convert'


def convert_currency(amount, from_currency, to_currency='RUB'):
    """
    Конвертирует сумму из from_currency в to_currency.
    Возвращает сконвертированную сумму или None при ошибке.
    """
    headers = {
        'apikey': API_KEY
    }
    params = {
        'from': from_currency,
        'to': to_currency,
        'amount': amount
    }
    response = requests.get(CONVERT_URL, headers=headers, params=params)
    if response.status_code == 200:
        data = response.json()
        # В ответе обычно есть поле 'result' с конвертированной суммой
        return data.get('result')
    else:
        print(f"Ошибка при запросе конвертации: {response.status_code}")
        return None


# Обрабатываем транзакции
for transaction in transactions:
    op_amount = transaction.get('operationAmount', {})
    amount_str = op_amount.get('amount', '0')
    currency_info = op_amount.get('currency', {})
    currency_code = currency_info.get('code', 'RUB')

    try:
        amount_value = float(amount_str)
    except ValueError:
        amount_value = 0.0

    if currency_code == 'RUB':
        # Уже в рублях
        print(amount_value)
    else:
        # Конвертируем в рубли
        converted_amount = convert_currency(amount_value, currency_code, 'RUB')
        if converted_amount is not None:
            print(converted_amount)
