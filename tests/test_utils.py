from src.utils import get_date, mask_account_number, mask_prepare_message_number, mask_card_number


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
