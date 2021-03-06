from gendiff.formatters.stylish import stylish
from gendiff.formatters.plain import plain
from gendiff.formatters.json import json_format


def format_(tree, format_name):
    match format_name:
        case 'stylish':
            return stylish(tree)
        case 'plain':
            return plain(tree)
        case 'json':
            return json_format(tree)
    raise ValueError("Non-existent format")
