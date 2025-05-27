from typing import List, Dict, Any

def filter_by_state(records: list[dict], state: str = 'EXECUTED') -> list[dict]:
    """
    Фильтрует список словарей по значению ключа 'state'.
    """
    filtered_records = []  # создаем пустой список для результатов
    for record in records:
        # получаем значение 'state' у текущего словаря
        current_state = record.get('state')
        # сравниваем его с переданным значением
        if current_state == state:
            # если совпадает, добавляем в результат
            filtered_records.append(record)
    return filtered_records


def sort_by_date(records: list[dict], reverse: bool = True) -> list[dict]:
    """
    Сортирует список словарей по дате в порядке убывания или возрастания.
    """
    # создаем копию списка для сортировки, чтобы не изменять исходный
    sorted_records = []

    # копируем исходный список
    for record in records:
        sorted_records.append(record)

    def get_date(record: Dict[str, Any]) -> str:
        # функция для получения даты из записи
        return record.get('date') or ''

    # сортируем список по дате
    sorted_records = sorted(sorted_records, key=get_date, reverse=reverse)

    return sorted_records
