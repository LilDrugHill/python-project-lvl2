import json
import yaml
from gendiff.formatters.json_format import json_format
from gendiff.formatters.plain import plain
from gendiff.formatters.stylish import stringify


def parse_input(file):
    if file[-4:] == 'json':
        file = convert_json(file)
    elif file[-4:] == 'yaml' or file[-3:] == 'yml':
        file = convert_yaml(file)
    else:
        raise ValueError("Wrong input format")

    return file


def convert_json(file):
    with open(file, encoding='utf-8') as read_file:
        file = json.load(read_file)

    return file


def convert_yaml(file):
    with open(file, encoding='utf-8') as read_file:
        file = yaml.safe_load(read_file)

    return file


def format(format_name, tree):
    if format_name is None or format_name == 'stylish':
        return stringify(tree)
    elif format_name == 'plain':
        return plain(tree)
    elif format_name == 'json':
        return json_format(tree)
    else:
        raise ValueError("Non-existent format")
