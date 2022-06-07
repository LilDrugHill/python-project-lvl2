import json


def convert(file):
    with open(file, encoding='utf-8') as read_file:
        file = json.load(read_file)

    return file
