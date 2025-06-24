import json
import os

filepath = "../data/operations.json"


def read_json_file(filepath):
    """
    Читает JSON-файл по указанному пути.
    Возвращает список словарей с данными о транзакциях.
    Если файл пустой, содержит не-список или не найден — возвращает пустой список.
    """
    if not os.path.exists(filepath):
        return []

    # Открываем файл по указанному пути в режиме чтения с кодировкой UTF-8
    try:
        with open(filepath, "r", encoding="utf-8") as file:
            # чтение данных из файла
            operation_data = json.load(file)
            if isinstance(operation_data, list):
                return operation_data
            else:
                return []
    except json.JSONDecodeError:
        return []


# transactions = read_json_file(filepath)
# print(transactions)
