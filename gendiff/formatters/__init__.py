from gendiff.formatters.stylish import stringify
from gendiff.formatters.plain import plain
from gendiff.formatters.json_format import json_format


def format(tree, format_name):
    match format_name:
        case 'stylish':
            return stringify(tree)
        case 'plain':
            return plain(tree)
        case 'json':
            return json_format(tree)
    raise ValueError("Non-existent format")
