import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


# Фикстура для базовых транзакций
@pytest.fixture
def transactions():
    return [
        {"id": 1, "operationAmount": {"amount": "1000", "currency": {"code": "USD"}}},
        {"id": 2, "operationAmount": {"amount": "2000", "currency": {"code": "EUR"}}},
        {"id": 3, "operationAmount": {"amount": "3000", "currency": {"code": "USD"}}},
    ]


@pytest.mark.parametrize(
    "currency_code, expected_ids",
    [
        ("USD", [1, 3]),
        ("EUR", [2]),
        ("JPY", []),
    ],
)
def test_filter_by_currency_with_params(transactions, currency_code, expected_ids):
    result = list(filter_by_currency(transactions, currency_code))
    result_ids = [t["id"] for t in result]
    assert result_ids == expected_ids


@pytest.mark.parametrize(
    "transactions, expected_descriptions",
    [
        (
            [
                {"description": "Перевод организации"},
                {"description": "Перевод со счета на счет"},
                {"description": "Перевод с карты на карту"},
                {"description": "Некоторое другое описание"},
            ],
            [
                "Перевод организации",
                "Перевод со счета на счет",
                "Перевод с карты на карту",
                "Некоторое другое описание",
            ],
        ),
        (
            [
                # в нижнем регистре
                {"description": "перевод организации"},
                {"description": "перевод со счета на счет"},
                # пустое описание
                {"description": ""},
            ],
            ["Перевод организации", "Перевод со счета на счет", "Описание не указано"],
        ),
        (
            [
                {"description": "другое описание"},
            ],
            ["Другое описание"],
        ),
    ],
)
def test_transaction_descriptions(transactions, expected_descriptions):
    gen = transaction_descriptions(transactions)
    for expected in expected_descriptions:
        assert next(gen) == expected


@pytest.mark.parametrize(
    "start, end, expected",
    [
        (1, 3, ["0000 0000 0000 0001", "0000 0000 0000 0002", "0000 0000 0000 0003"]),
        (9999999999999998, 9999999999999999, ["9999 9999 9999 9998", "9999 9999 9999 9999"]),
    ],
)
def test_generator_edge_cases(start, end, expected):
    result = list(card_number_generator(start, end))

    # Проверка, что количество номеров соответствует диапазону
    assert len(result) == (end - start + 1)

    # Проверка, что номера соответствуют крайним значениям
    assert result[0].split()[-1] == str(start % 10000).zfill(4)
    # Последний номер — число end
    assert result[-1].split()[-1] == str(end % 10000).zfill(4)

    # Проверка формата каждого номера
    for number in result:
        parts = number.split()
        assert len(parts) == 4
        for part in parts:
            assert len(part) == 4
            assert part.isdigit()
