import requests

from src.utils import read_json_file

filepath = "../data/operations.json"
transactions = read_json_file(filepath)
print(transactions)

API_KEY = '13efaghyEH1cPaWtvn1Vw7yXfA7OI0e7'
BASE_URL = 'https://api.apilayer.com/exchangerates_data/latest'


def get_exchange_rate(currency):
    """
    Получает текущий курс обмена для указанной валюты к рублю.
    Возвращает курс как float.
    """
    headers = {
        'apikey': API_KEY
    }
    params = {
        'base': 'RUB',
        'symbols': currency
    }
    response = requests.get(BASE_URL, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()
        print("Ответ API:", data)

        rate = data['rates'].get(currency)
        if rate:
            return rate
        else:
            print(f"Курс для {currency} не найден.")
            return None
    else:
        print(f"Ошибка при запросе курса: {response.status_code}")
        return None


def get_transaction_amount_in_rub(transaction, exchange_rates):
    """
    Принимает транзакцию и возвращает сумму в рублях (float).
    Использует переданный словарь курсов.
    """
    op_amount = transaction.get('operationAmount', {})
    amount_str = op_amount.get('amount', '0')
    currency_info = op_amount.get('currency', {})
    currency_code = currency_info.get('code', 'RUB')

    # Преобразуем сумму из строки в float
    try:
        amount_value = float(amount_str)
    except ValueError:
        amount_value = 0.0

    # Конвертация
    if currency_code == 'RUB':
        return amount_value
    elif currency_code in ('USD', 'EUR'):
        rate = exchange_rates.get(currency_code)
        if rate:
            return amount_value * rate
        else:
            print(f"Курс для {currency_code} не найден.")
            return 0.0
    else:
        print(f"Необработанная валюта: {currency_code}")
        return 0.0


# Получаем курсы один раз перед циклом
exchange_rates = {}
for curr in ['USD', 'EUR']:
    rate = get_exchange_rate(curr)
    if rate:
        exchange_rates[curr] = rate

# Обрабатываем транзакции
for transaction in transactions:
    amount_in_rub = get_transaction_amount_in_rub(transaction, exchange_rates)
    print(amount_in_rub)
