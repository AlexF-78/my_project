# Обработка данных транзакций

Этот проект содержит функции для обработки списка транзакций в виде словарей.

## Цель проекта

Реализовать функции фильтрации и сортировки данных транзакций по статусу и дате.

## Структура проекта

- `src/processing.py` - модуль с функциями обработки данных.

## Установка и использование

Требования
Python 3.8 или выше
Виртуальная среда (рекомендуется)

## Установка зависимостей

Данный проект не использует сторонних внешних библиотек, кроме стандартной библиотеки Python.

## Установка проекта
Клонируйте репозиторий или скопируйте файлы в свою директорию.
Активируйте виртуальную среду.

## Использование
Импортируйте функции из модуля processing:
from src.processing import filter_by_state, sort_by_date
Далее используйте их для обработки данных транзакций.

## Новые функции в модуле src/generators.py
Этот модуль содержит генераторы для создания тестовых данных и фильтрации транзакций по валюте и описанию.

## Функции:
1. filter_by_currency
Генерирует транзакции из списка, у которых валюта совпадает с заданным кодом.

transactions = [...]  # список транзакций
for transaction in filter_by_currency(transactions, 'USD'):
    print(transaction)

2. transaction_descriptions
Генерирует описание каждой транзакции на основе её содержимого.

for description in transaction_descriptions(transactions):
    print(description)```

3. card_number_generator
Генерирует последовательность номеров карт в формате 'XXXX XXXX XXXX XXXX'.

for card_number in card_number_generator(0000000000000001, 0000000000000010):
    print(card_number)

Необходимо скопировать .env.example в .env и заполнить свои значения.

## В проект добавлен новый модуль с фунциями: 
1. read_csv_file
Читает CSV файл с финансовыми операциями и возвращает список словарей.

2. read_xlsx_file
Читает XLSX файл с финансовыми операциями и возвращает список словарей.

## Новые функции:

## Поиск операций (`src/bank_operations.py`)
```python
def process_bank_search(data: list[dict], search: str) -> list[dict]:
    """
    Ищет операции по строке в описании (регистронезависимо)
    
    Аргументы:
        data: Список операций
        search: Строка для поиска
        
    Возвращает:
        Список операций, содержащих искомую строку
    """


#### Подсчет операций по категориям (`src/bank_processing.py`)

class Поиск:
pass

```python
def process_bank_operations(data: list[dict], categories: list[str]) -> dict[str, int]:
    """
    Считает количество операций по категориям
    
    Аргументы:
        data: Список операций
        categories: Список категорий для поиска
        
    Возвращает:
        Словарь {категория: количество}
    """

## Примеры использования

1. Поиск операций:
```python
from src.bank_operations import process_bank_search

result = process_bank_search(transactions, "перевод")

2. Анализ по категориям:
```python
from src.bank_processing import process_bank_operations

stats = process_bank_operations(transactions, ["перевод", "оплата"])


## Требования
- Python 3.8+
- Зависимости: `pandas`, `pytest`, `python-dateutil`

Установка зависимостей:
```bash
pip install -r requirements.txt