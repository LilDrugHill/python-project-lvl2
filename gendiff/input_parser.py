import json
import yaml
from os import path


def get_data(file_path):
    with open(file_path, encoding='utf-8') as data:
        data_format = path.splitext(file_path)[1][1:]
        return parse(data, data_format)


def parse(data, data_format):

    if data_format == 'json':
        formated_data = json.load(data)
    elif data_format == 'yaml' or data_format == 'yml':
        formated_data = yaml.safe_load(data)
    else:
        raise ValueError("Wrong input format")

    return formated_data
