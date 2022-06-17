from formatters.json_format import json_format
from formatters.plain import plain
from formatters.stylish import stringify


def change_format(args, diff_tree):
    if args.format is None:
        return stringify(diff_tree)
    elif args.format == 'plain':
        return plain(diff_tree)
    elif args.format == 'json':
        return json_format(diff_tree)
