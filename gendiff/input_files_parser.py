import json
import yaml


def parse_input_format(file1, file2):
    if file1[-4:] == 'json':
        file1 = convert_json(file1)
    elif file1[-4:] == 'yaml' or file1[-3:] == 'yml':
        file1 = convert_yaml(file1)
    else:
        raise ValueError("Wrong input format (first file)")

    if file2[-4:] == 'json':
        file2 = convert_json(file2)
    elif file2[-4:] == 'yaml' or file2[-4:] == 'yml':
        file2 = convert_yaml(file2)
    else:
        raise ValueError("Wrong input format (second file)")

    return file1, file2


def convert_json(file):
    with open(file, encoding='utf-8') as read_file:
        file = json.load(read_file)

    return file


def convert_yaml(file):
    with open(file, encoding='utf-8') as read_file:
        file = yaml.safe_load(read_file)

    return file
