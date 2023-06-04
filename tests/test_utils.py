from utils import get_data, get_filtered_data, get_last_values, get_formatted_data


def test_get_data():
    data = get_data()
    assert isinstance(data, list)
    assert data is not None

def test_get_filtered_data(item):
    assert  get_filtered_data(item, filter_empty_from=True) == [{
    "id": 441945886,
    "state": "EXECUTED",
    "date": "2019-08-26T10:50:58.294041",
    "operationAmount": {
      "amount": "31957.58",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Перевод организации",
    "from": "Maestro 1596837868705199",
    "to": "Счет 64686473678894779589"
  }]
    assert get_filtered_data(item) == [
  {
    "id": 441945886,
    "state": "EXECUTED",
    "date": "2019-08-26T10:50:58.294041",
    "operationAmount": {
      "amount": "31957.58",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Перевод организации",
    "from": "Maestro 1596837868705199",
    "to": "Счет 64686473678894779589"
  },
  {
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
            "description": "Открытие вклада",
            "to": "Счет 11776614605963066702"
        }]


def test_get_last_values(item2):
    datas = [x["date"] for x in get_last_values(item2, 3)]
    assert datas == ["2019-08-26T10:50:58.294041", "2019-07-03T18:35:29.512364", "2018-06-30T02:08:58.425572"]


def test_get_formatted_data(item2):
    data = get_formatted_data(item2)
    assert data == ['03.07.2019 Перевод организации\nMasterCard 7158 30** **** 6758 -> Счет **5560\n8221.37 USD',
                    '26.08.2019 Перевод организации\nMaestro 1596 83** **** 5199 -> Счет **9589\n31957.58 руб.',
                    '30.06.2018 Открытие вклада\n  -> Счет **6702\n9824.07 USD']


