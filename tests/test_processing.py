import pytest
from src.processing import filter_by_state, sort_by_date

# Фикстуры с тестовыми данными
@pytest.fixture
def sample_records():
    return [
        {'id': 1, 'state': 'EXECUTED', 'date': '2023-10-05T14:30:00'},
        {'id': 2, 'state': 'PENDING', 'date': '2023-09-15T09:20:00'},
        {'id': 3, 'state': 'EXECUTED', 'date': '2023-10-01T12:00:00'},
        {'id': 4, 'state': 'CANCELLED', 'date': '2023-08-20T16:45:00'},
        {'id': 5, 'state': 'EXECUTED', 'date': None},
        {'id': 6, 'state': None, 'date': '2023-07-10T11:11:11'},
    ]

# Тесты для filter_by_state
@pytest.mark.parametrize("state, expected_ids", [
    ('EXECUTED', [1, 3, 5]),
    ('PENDING', [2]),
    ('CANCELLED', [4]),
    ('NON_EXISTENT', []),
])
def test_filter_by_state(sample_records, state, expected_ids):
    result = filter_by_state(sample_records, state)
    result_ids = [record['id'] for record in result]
    assert result_ids == expected_ids

# Тест на отсутствие совпадений
def test_filter_by_state_no_matches(sample_records):
    result = filter_by_state(sample_records, 'NON_EXISTENT')
    assert result == []

# Тест с пустым списком
def test_filter_by_state_empty():
    assert filter_by_state([], 'EXECUTED') == []

# Тест с None в списке (если такие возможны)
def test_filter_by_state_with_none():
    records = [{'id': 1, 'state': None}]
    result = filter_by_state(records, None)
    assert result == records

# Тестирование sort_by_date
@pytest.fixture
def sample_dates():
    return [
        {'id': 1, 'date': '2023-10-05T14:30:00'},
        {'id': 2, 'date': '2023-09-15T09:20:00'},
        {'id': 3, 'date': '2023-10-01T12:00:00'},
        {'id': 4, 'date': None},
        {'id': 5, 'date': ''},
        {'id': 6},  # без ключа date
        {'id': 7, 'date': '2023-07-10T11:11:11'},
        {'id': 8, 'date': 'invalid-date'},  # некорректный формат
    ]

# Проверка сортировки по убыванию (по умолчанию)
def test_sort_by_date_descending(sample_dates):
    sorted_list = sort_by_date(sample_dates)
    dates = [record.get('date') for record in sorted_list]
    valid_dates = [d for d in dates if d]
    assert valid_dates == sorted(valid_dates, reverse=True)

# Проверка сортировки по возрастанию
def test_sort_by_date_ascending(sample_dates):
    sorted_list = sort_by_date(sample_dates, reverse=False)
    dates = [record.get('date') for record in sorted_list]
    valid_dates = [d for d in dates if d]
    assert valid_dates == sorted(valid_dates)

# Тест с одинаковыми датами
def test_sort_with_equal_dates():
    records = [
        {'id': 1, 'date': '2023-10-05T14:30:00'},
        {'id': 2, 'date': '2023-10-05T14:30:00'},
        {'id': 3, 'date': None},
        {'id': 4},
        {'id': 5, 'date':'2022-01-01T00:00:00'}
    ]
    sorted_desc = sort_by_date(records)
    # Проверяем что первые два элемента имеют одинаковую дату (или равны по порядку)
    assert sorted_desc[0]['date'] >= sorted_desc[1]['date']

# Тест некорректных дат (функция должна сортировать их как пустые строки или в конец)
def test_sort_with_invalid_dates():
    records = [
        {'id':'a', 'date':'not-a-date'},
        {'id':'b', 'date':'2023-12-01T12:00:00'}
    ]
    result_desc = sort_by_date(records)
    assert result_desc[0]['date'] == "2023-12-01T12:00:00"