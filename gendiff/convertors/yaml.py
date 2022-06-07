import yaml


def convert(file):
    with open(file, encoding='utf-8') as read_file:
        file = yaml.safe_load(read_file)

    return file
