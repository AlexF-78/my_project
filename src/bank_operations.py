import re
from typing import Dict, List

from src.read_xlsx_csv import csv_transactions, xlsx_transactions


def process_bank_search(data: List[Dict], search: str) -> List[Dict]:
    """
    Фильтрует операции по строке поиска в описании (регистронезависимо).
    """
    if not data or not search:
        return []

    try:
        pattern = re.compile(re.escape(search), re.IGNORECASE)
    except re.error:
        return []

    result = []
    for operation in data:
        description = operation.get('description', '')
        if description and pattern.search(description):
            result.append(operation)

    return result


def search_in_all_transactions(search: str) -> Dict[str, List[Dict]]:
    """
    Ищет операции в обоих источниках данных
    """
    return {
        'csv': process_bank_search(csv_transactions, search),
        'xlsx': process_bank_search(xlsx_transactions, search)
    }
