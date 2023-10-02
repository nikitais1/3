from src.utils import get_date, mask_account_number, mask_prepare_message_number, mask_card_number, \
    prepare_user_message, filter_and_sorting


def test_get_date():
    assert get_date("2019-07-13T18:51:29.313309") == "13.07.2019"
    assert get_date("2018-03-09T23:57:37.537412") == "09.03.2018"


def test_mask_prepare_message_number():
    assert mask_prepare_message_number("Maestro 1308795367077170") == "Maestro 1308 79** **** 7170"
    assert mask_prepare_message_number("Счет 46363668439560358409") == "Счет **8409"
    assert mask_prepare_message_number(None) == "Личный счет"


def test_mask_card_number():
    assert mask_card_number("1308795367077170") == "1308 79** **** 7170"
    assert mask_card_number("130879536707710") == "Проверьте правильность введенных данных"


def test_mask_account_number():
    assert mask_account_number("46363668439560358409") == "**8409"
    assert mask_account_number("4636366843956035840") == "Проверьте правильность введенных данных"


def test_prepare_user_message():
    test_data = {'id': 863064926,
                 'state': 'EXECUTED',
                 'date': '2019-12-08T22:46:21.935582',
                 'operationAmount': {'amount': '41096.24',
                                     'currency': {'name': 'USD',
                                                  'code': 'USD'}},
                 'description': 'Открытие вклада',
                 'to': 'Счет 90424923579946435907'}
    assert prepare_user_message(test_data) == "08.12.2019 Открытие вклада\nЛичный счет -> Счет **5907\n41096.24 USD\n"


def test_filter_and_sorting():
    test_data = [{'id': 441945886,
                 'state': 'EXECUTED',
                 'date': '2019-08-26T10:50:58.294041',
                 'operationAmount': {'amount': '31957.58',
                                     'currency': {'name': 'руб.',
                                                  'code': 'RUB'}},
                 'description': 'Перевод организации',
                 'from': 'Maestro 1596837868705199',
                 'to': 'Счет 64686473678894779589'},
                {'id': 619287771,
                 'state': 'EXECUTED',
                 'date': '2019-08-19T16:30:41.967497',
                 'operationAmount': {'amount': '81150.87',
                                     'currency': {'name': 'USD',
                                                  'code': 'USD'}},
                 'description': 'Перевод организации',
                 'from': 'Счет 17691325653939384901',
                 'to': 'Счет 49304996510329747621'},
                 {'id': 390558607,
                  'state': 'CANCELED',
                  'date': '2019-02-12T00:08:07.524972',
                  'operationAmount': {'amount': '16796.95',
                                      'currency': {'name': 'USD',
                                                   'code': 'USD'}},
                  'description': 'Перевод организации',
                  'from': 'Счет 72645194281643232984',
                  'to': 'Счет 95782287258966264115'}]

    test_01 = filter_and_sorting(test_data)
    assert len(test_01) == 2
    assert test_01[0]['id'] == 441945886
