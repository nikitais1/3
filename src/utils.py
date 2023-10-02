def filter_and_sorting(data: list):
    """Принимает список всех операций, достает успешные,
    сортирует их по дате, складывает в новый список и возвращает его"""
    items = [item for item in data if item.get('state') == "EXECUTED"]
    items.sort(key=lambda x: x.get('date'), reverse=True)
    return items


def get_date(date: str):
    """Принимает строку с датой, редактирует и возвращиет ее в нужном формате"""
    date_num = date[0:10].split('-')
    return date_num[2] + '.' + date_num[1] + '.' + date_num[0]


def mask_prepare_message_number(message):
    """Определяет карта или счет"""
    if message is None:
        return 'Личный счет'

    message_split = message.split(' ')
    if message_split[0] == 'Счет':
        hidden_number = mask_account_number(message_split[-1])
    else:
        hidden_number = mask_card_number(message_split[-1])

    return ' '.join(message_split[:-1]) + ' ' + hidden_number


def mask_card_number(number: str):
    """Маскирует номер карты и возвращает результат"""
    if number.isdigit() and len(number) == 16:
        return number[:4] + ' ' + number[4:6] + '** **** ' + number[-4:]


def mask_account_number(number: str):
    """Маскирует номер счета и возвращает результат"""
    if number.isdigit() and len(number) == 20:
        return '**' + number[-4:]


def prepare_user_message(item: dict):
    """Выводит информацию по операции"""
    date = get_date(item.get('date'))
    desc = item.get('description')
    from_ = mask_prepare_message_number(item.get('from'))
    to_ = mask_prepare_message_number(item.get('to'))
    amount = item.get('operationAmount').get('amount')
    curr = item.get('operationAmount').get('currency').get('name')

    return f"{date} {desc}\n{from_} -> {to_}\n{amount} {curr}\n"
