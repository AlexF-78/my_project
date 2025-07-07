from collections import Counter
from typing import Dict, List

from src.read_xlsx_csv import csv_transactions, xlsx_transactions


def process_bank_operations(data: List[Dict], categories: List[str]) -> Dict[str, int]:
    """
    Подсчитывает количество операций для каждой категории из списка categories.
    Категория определяется по точному совпадению в поле 'description'.
    Возвращает словарь {категория: количество}.

    Args:
        data: Список словарей с банковскими операциями
        categories: Список категорий для поиска

    Returns:
        Словарь с количеством операций по каждой категории
    """
    if not data or not categories:
        return {}

    # Создаем счетчик для категорий
    category_counter = Counter()

    # Приводим категории к нижнему регистру для регистронезависимого сравнения
    categories_lower = [cat.lower() for cat in categories]

    for operation in data:
        description = operation.get('description', '').lower()
        for category in categories_lower:
            if category in description:
                category_counter[category] += 1
                break

    # Возвращаем результат с оригинальными названиями категорий
    return {categories[i]: category_counter[cat]
            for i, cat in enumerate(categories_lower)}


def get_operations_by_categories(categories: List[str]) -> Dict[str, Dict[str, int]]:
    """
    Обрабатывает операции из CSV и XLSX файлов и возвращает статистику по категориям

    Args:
        categories: Список категорий для анализа

    Returns:
        Словарь с результатами для CSV и XLSX данных
    """
    csv_result = process_bank_operations(csv_transactions, categories)
    xlsx_result = process_bank_operations(xlsx_transactions, categories)

    return {
        'csv': csv_result,
        'xlsx': xlsx_result
    }
