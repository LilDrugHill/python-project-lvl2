from formatters.json_format import json_format
from formatters.plain import plain
from formatters.stylish import stringify


def choose_format(format, diff_tree):
    if format is None or format == 'stylish':
        return stringify(diff_tree)
    elif format == 'plain':
        return plain(diff_tree)
    elif format == 'json':
        return json_format(diff_tree)
