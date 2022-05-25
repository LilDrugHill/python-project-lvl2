import json


def convert_json(file):
    with open(file) as read_file:
        file = json.load(read_file)

    return file
