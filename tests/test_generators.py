import pytest

from src.generators import filter_by_currency, transaction_descriptions


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
