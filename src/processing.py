from datetime import datetime
from typing import Any, Dict


def filter_by_state(records: list[dict], state: str = "EXECUTED") -> list[dict]:
    """
    Фильтрует список словарей по значению ключа 'state'.
    """
    filtered_records = []  # создаем пустой список для результатов
    for record in records:
        # получаем значение 'state' у текущего словаря
        current_state = record.get("state")
        # сравниваем его с переданным значением
        if current_state == state:
            # если совпадает, добавляем в результат
            filtered_records.append(record)
    return filtered_records


def parse_date(record: dict) -> datetime:
    """
    Парсит дату из строки в объект datetime.
    Если дата отсутствует или некорректна, выбрасывает ValueError.
    """
    date_str = record.get("date")
    if not isinstance(date_str, str) or not date_str:
        raise ValueError(f"Invalid date format: {date_str}")
    try:
        return datetime.fromisoformat(date_str)
    except ValueError:
        raise ValueError(f"Invalid date format: {date_str}")


def sort_by_date(records: list[dict], reverse: bool = True) -> list[dict]:
    """
    Сортирует список по дате.
    Если дата некорректна или отсутствует, выбрасывает исключение.
    """

    def key_func(record):
        return parse_date(record)

    return sorted(records, key=key_func, reverse=reverse)
