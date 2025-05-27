def filter_by_state(records: list, state='EXECUTED')-> list:
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
