import pytest

from src.generators import filter_by_currency


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
