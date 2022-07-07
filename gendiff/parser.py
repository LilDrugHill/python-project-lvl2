import json
from os import path

import yaml


def get_data(file_path):
    with open(file_path, encoding='utf-8') as data:
        data_format = path.splitext(file_path)[1][1:]
        return parse(data, data_format)


def parse(data, data_format):

    if data_format == 'json':
        return json.load(data)
    if data_format in ('yaml', 'yml'):
        return yaml.safe_load(data)
    raise ValueError('Wrong input format. Use yml/yaml or json formats')
