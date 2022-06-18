import json
import yaml


def parse_input_format(args):
    if args.first_file[-4:] == 'json':
        file1 = convert_json(args.first_file)
    elif args.second_file[-4:] == 'yaml' or args.second_file[-3:] == 'yml':
        file1 = convert_yaml(args.first_file)
    else:
        raise ValueError("Wrong input format (first file)")

    if args.second_file[-4:] == 'json':
        file2 = convert_json(args.second_file)
    elif args.second_file[-4:] == 'yaml' or args.second_file[-4:] == 'yml':
        file2 = convert_yaml(args.second_file)
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
