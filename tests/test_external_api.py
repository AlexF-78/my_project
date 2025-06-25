from unittest.mock import MagicMock, patch

from src.external_api import get_exchange_rate, get_transaction_amount_in_rub


@patch("src.external_api.requests.get")
def test_get_exchange_rate_success(mock_get):
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"rates": {"USD": 75.0}}
    mock_get.return_value = mock_response

    rate = get_exchange_rate("USD")
    assert rate == 75.0
    mock_get.assert_called_once()


@patch("src.external_api.requests.get")
def test_get_exchange_rate_failure_status(mock_get):
    mock_response = MagicMock()
    mock_response.status_code = 500
    mock_get.return_value = mock_response

    rate = get_exchange_rate("USD")
    assert rate is None


@patch("src.external_api.requests.get")
def test_get_exchange_rate_no_rate_in_response(mock_get):
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"rates": {}}
    mock_get.return_value = mock_response

    rate = get_exchange_rate("USD")
    assert rate is None


def test_get_transaction_amount_in_rub_rub_currency():
    transaction = {"operationAmount": {"amount": "100", "currency": {"code": "RUB"}}}
    exchange_rates = {}
    result = get_transaction_amount_in_rub(transaction, exchange_rates)
    assert result == 100.0


def test_get_transaction_amount_in_rub_usd_with_rate():
    transaction = {"operationAmount": {"amount": "10", "currency": {"code": "USD"}}}
    exchange_rates = {"USD": 75}
    result = get_transaction_amount_in_rub(transaction, exchange_rates)
    assert result == 10 * 75


def test_get_transaction_amount_in_rub_usd_no_rate():
    transaction = {"operationAmount": {"amount": "10", "currency": {"code": "USD"}}}
    exchange_rates = {}
    result = get_transaction_amount_in_rub(transaction, exchange_rates)
    assert result == 0.0


def test_get_transaction_amount_in_rub_invalid_amount():
    transaction = {"operationAmount": {"amount": "abc", "currency": {"code": "RUB"}}}  # Некорректное значение суммы
    exchange_rates = {}
    result = get_transaction_amount_in_rub(transaction, exchange_rates)
    assert result == 0.0
