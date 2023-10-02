import json

from src.utils import filter_and_sorting, prepare_user_message

with open('../data/operations.json', 'r', encoding='utf-8') as file:
    data = json.load(file)
items = filter_and_sorting(data)
for i in range(5):
    print(prepare_user_message(items[i]))


