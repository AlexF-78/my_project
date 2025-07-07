from datetime import datetime
from typing import Dict, List

from src.bank_operations import process_bank_search
from src.bank_processing import process_bank_operations
from src.read_xlsx_csv import csv_transactions, xlsx_transactions
from src.utils import json_transactions


def filter_by_status(data: List[Dict], status: str) -> List[Dict]:
    """Фильтрует операции по статусу, проверяя оба возможных поля ('state' и 'status')"""
    filtered = []
    for op in data:
        # Проверяем оба возможных названия поля  'state' и 'status
        op_status = str(op.get("state", op.get("status", ""))).lower()
        if op_status == status.lower():
            filtered.append(op)
    return filtered


def sort_operations(data: List[Dict], reverse: bool = False) -> List[Dict]:
    """Сортирует операции по дате с преобразованием строки в datetime"""

    def get_date(op):
        date_str = op.get("date", "")
        try:
            return datetime.fromisoformat(date_str)
        except (ValueError, TypeError):
            # Для операций без даты
            return datetime.min

    return sorted(data, key=get_date, reverse=reverse)


def filter_by_currency(data: List[Dict], currency: str = "RUB") -> List[Dict]:
    """Фильтрует операции по валюте"""
    return [op for op in data if str(op.get("currency", "")).upper() == currency.upper()]


def print_operations(operations: List[Dict]):
    """Печатает список операций"""
    if not operations:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
        return

    print(f"\nВсего банковских операций в выборке: {len(operations)}\n")
    for op in operations:
        date = op.get("date", "Дата неизвестна")
        desc = op.get("description", "Описание отсутствует")
        amount = op.get("amount", "")
        currency = op.get("currency", "")

        print(f"{date} {desc}")
        if "from" in op:
            print(f"{op['from']} -> {op.get('to', '')}")
        elif "to" in op:
            print(f"Счет **{op['to'][-4:]}")

        print(f"Сумма: {amount} {currency}\n")


def print_category_stats(stats: Dict[str, int]):
    """Печатает статистику по категориям"""
    if not stats:
        print("Нет данных для отображения статистики")
        return

    print("\nСтатистика по категориям:")
    for category, count in stats.items():
        print(f"{category}: {count} операций")
    print()


def get_user_choice(prompt: str, options: List[str]) -> str:
    """Получает выбор пользователя с валидацией"""
    while True:
        choice = input(prompt).strip().lower()
        if choice in options:
            return choice
        print(f"Некорректный ввод. Допустимые варианты: {', '.join(options)}")


def main():
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")

    # Выбор источника данных
    source = get_user_choice(
        "Выберите необходимый пункт меню:\n"
        "1. Получить информацию о транзакциях из JSON-файла\n"
        "2. Получить информацию о транзакциях из CSV-файла\n"
        "3. Получить информацию о транзакциях из XLSX-файла\n",
        ["1", "2", "3"],
    )

    # Загрузка данных
    if source == "1":
        print("Для обработки выбран JSON-файл.")
        data = json_transactions
        # print(data)
    elif source == "2":
        print("Для обработки выбран CSV-файл.")
        data = csv_transactions
        # print(data)
    else:
        print("Для обработки выбран XLSX-файл.")
        data = xlsx_transactions
        # print(data)
    if not data:
        print("Не удалось загрузить данные. Программа завершена.")
        return

    # Фильтрация по статусу
    valid_statuses = ["executed", "canceled", "pending"]
    while True:
        status = (
            input(
                "Введите статус, по которому необходимо выполнить фильтрацию.\n"
                "Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING\n"
            )
            .strip()
            .lower()
        )

        if status in valid_statuses:
            filtered_data = filter_by_status(data, status)
            # Если операций не найдено
            if not filtered_data:
                print(f"\nОпераций со статусом '{status.upper()}' не найдено.")
                print("Пожалуйста, выберите другой статус.\n")
                # Возвращаемся к выбору статуса
                continue

            print(f'Операции отфильтрованы по статусу "{status.upper()}"')

            # Отладочная информация
            print("\nПримеры операций:")
            for op in filtered_data[:3]:
                print(f"- {op.get('description')} (Статус: {op.get('state')})")

            print(f"\nВсего найдено операций: {len(filtered_data)}")
            break
        else:
            print(f'Статус операции "{status}" недоступен.')

    # Дополнительные фильтры
    sort_choice = get_user_choice("Отсортировать операции по дате? Да/Нет\n", ["да", "нет"])
    if sort_choice == "да":
        order = get_user_choice("Отсортировать по возрастанию или по убыванию?\n", ["по возрастанию", "по убыванию"])
        filtered_data = sort_operations(filtered_data, order == "по убыванию")

    currency_choice = get_user_choice("Выводить только рублевые транзакции? Да/Нет\n", ["да", "нет"])
    if currency_choice == "да":
        filtered_data = filter_by_currency(filtered_data, "RUB")

    search_choice = get_user_choice(
        "Отфильтровать список транзакций по определенному слову в описании? Да/Нет\n", ["да", "нет"]
    )
    if search_choice == "да":
        search_word = input("Введите слово для поиска в описании:\n").strip()
        filtered_data = process_bank_search(filtered_data, search_word)

    # Вывод результатов
    print("\nРаспечатываю итоговый список транзакций...")
    print_operations(filtered_data)


if __name__ == "__main__":
    main()
