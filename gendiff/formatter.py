from gendiff.formatters.stylish import stringify
from gendiff.formatters.plain import plain
from gendiff.formatters.json_format import json_format


def format(tree, format_name):
    if format_name == 'stylish' or not format_name:
        return stringify(tree)
    elif format_name == 'plain':
        return plain(tree)
    elif format_name == 'json':
        return json_format(tree)

    raise ValueError("Non-existent format")
