import json
import os

from src.logging_config import logging

logger = logging.getLogger('utils')

filepath = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                          "data", "operations.json")
logger.info("Запуск модуля utils.py")


def read_json_file(filepath):
    """
    Читает JSON-файл по указанному пути.
    Возвращает список словарей с данными о транзакциях.
    Если файл пустой, содержит не-список или не найден — возвращает пустой список.
    """

    logger.info(f"Попытка чтения файла: {filepath}")

    if not os.path.exists(filepath):
        logger.error(f"Файл не найден: {filepath}")
        return []

    # Открываем файл по указанному пути в режиме чтения с кодировкой UTF-8
    try:
        with open(filepath, "r", encoding="utf-8") as file:
            # чтение данных из файла
            operation_data = json.load(file)
            if isinstance(operation_data, list):
                logger.info(f"Успешно загружено {len(operation_data)} операций")
                return operation_data
            logger.warning("Файл не содержит список операций")
            # else:
            return []
    except (json.JSONDecodeError, OSError) as e:
        logger.error(f"Ошибка чтения файла {filepath}: {e}")
        return []


json_transactions = read_json_file(filepath)
# print(json_transactions)
