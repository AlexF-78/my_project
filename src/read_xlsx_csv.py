import os

import pandas as pd

# Получаем путь к папке my_project
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Создаём полный путь к файлу transaction.csv
file_csv_path = os.path.join(base_dir, "data", "transactions.csv")

# Создаём полный путь к файлу transaction_excel.xlsx
file_xlsx_path = os.path.join(base_dir, "data", "transactions_excel.xlsx")


def parse_raw_data(transactions):
    """
    Преобразует данные из формата {'field1;field2': 'value1;value2'}
    в нормальные словари [{'field1': 'value1', 'field2': 'value2'}]
    """
    parsed_data = []
    for item in transactions:
        # Получаем ключ (строку с названиями полей)
        fields_str = list(item.keys())[0]
        # Получаем значения
        values_str = item[fields_str]

        # Разделяем поля и значения
        fields = fields_str.split(';')
        values = values_str.split(';')

        # Создаем словарь операции
        operation = dict(zip(fields, values))
        parsed_data.append(operation)

    return parsed_data


def read_csv_file(file_path):
    """
    Читает CSV файл с финансовыми операциями и возвращает список словарей.
    """

    try:
        df = pd.read_csv(file_path)
        # Преобразуем DataFrame в список словарей
        transactions = df.to_dict(orient="records")
        return parse_raw_data(transactions)
    except Exception as e:
        print(f" Ошибка при чтении CSV файла: {e}")
        return []


def read_xlsx_file(file_path):
    """
    Читает XLSX файл с финансовыми операциями и возвращает список словарей
    """
    try:
        df = pd.read_excel(file_path)
        # Преобразуем DataFrame в список словарей
        transactions = df.to_dict(orient="records")
        return transactions
    except Exception as e:
        print(f"Ошибка при чтении XLSX файла: {e}")
        return []


# Использование
csv_transactions = read_csv_file(file_csv_path)
# print(csv_transactions)

xlsx_transactions = read_xlsx_file(file_xlsx_path)
# print(xlsx_transactions)
