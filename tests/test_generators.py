import pytest
from src.generators import filter_by_currency, transaction_descriptions, card_number_generator


@pytest.fixture
def transactions():
    return [{
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {
            "amount": "9824.07",
            "currency": {
                "name": "USD",
                "code": "USD"
            }
        },
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702"
    },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {
                "amount": "79114.93",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188"
        }
    ]


def test_filter_by_currency_all(transactions):
    result = filter_by_currency(transactions, 'RUB')
    assert result


def test_filter_by_currency_not_data(transactions):
    with pytest.raises(AssertionError):
        assert filter_by_currency([], "EUR") == "Список пуст"


@pytest.mark.parametrize('index, expected', [(0, 'Перевод организации'), (1, 'Перевод со счета на счет')])
def test_transaction_descriptions_exp(index, expected):
    transactions = [

        {'description': 'Перевод организации'},

        {'description': 'Перевод со счета на счет'}

    ]
    descriptions = list(transaction_descriptions(transactions))
    assert descriptions[index] == expected


def test_filter_by_currency_empty():
    with pytest.raises(StopIteration):
        transaction = transaction_descriptions([])
        assert next(transaction) == "Транзакций нет"


@pytest.mark.parametrize('start, stop, expected', [(1, 2, ['0000 0000 0000 0001', '0000 0000 0000 0002'])])
def test_card_number_generator(start, stop, expected):
    result = list(card_number_generator(start, stop))
    assert result == expected


@pytest.mark.parametrize('start, stop, expected', [(9999999999999998, 9999999999999999,
                                                    ['9999 9999 9999 9998', '9999 9999 9999 9999'])])
def test_card_number_generator(start, stop, expected):
    result = list(card_number_generator(start, stop))
    assert result == expected

