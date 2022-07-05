import json
import yaml
from os import path
import sys


def get_data(file_path):
    try:
        with open(file_path, encoding='utf-8') as data:
            data_format = path.splitext(file_path)[1][1:]
            return parse(data, data_format)
    except FileNotFoundError:
        print("Wrong input format. Use yaml/yml or json formats.")
        sys.exit()


def parse(data, data_format):

    if data_format == 'json':
        return json.load(data)
    elif data_format == 'yaml' or data_format == 'yml':
        return yaml.safe_load(data)
