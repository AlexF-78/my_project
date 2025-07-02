import os

import pandas as pd

# Получаем путь к папке my_project
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Создаём полный путь к файлу transaction.csv
file_csv_path = os.path.join(base_dir, "data", "transactions.csv")

# Создаём полный путь к файлу transaction_excel.xlsx
file_xlsx_path = os.path.join(base_dir, "data", "transactions_excel.xlsx")


def read_csv_file(file_path):
    """
    Читает CSV файл с финансовыми операциями и возвращает список словарей.
    """

    try:
        df = pd.read_csv(file_path)
        # Преобразуем DataFrame в список словарей
        transactions = df.to_dict(orient="records")
        return transactions
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
print(csv_transactions)

xlsx_transactions = read_xlsx_file(file_xlsx_path)
print(xlsx_transactions)
