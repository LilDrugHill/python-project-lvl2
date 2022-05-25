import yaml


def convert_yaml(file):
    with open(file) as read_file:
        file = yaml.safe_load(read_file)

    return file
