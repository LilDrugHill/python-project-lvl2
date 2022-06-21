from formatters.json_format import json_format
from formatters.plain import plain
from formatters.stylish import stringify


def format(format_name, tree):
    if format_name is None or format_name == 'stylish':
        return stringify(tree)
    elif format_name == 'plain':
        return plain(tree)
    elif format_name == 'json':
        return json_format(tree)
