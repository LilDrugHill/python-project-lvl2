#!/usr/bin/env python

import argparse
from gendiff.comparator import generate_diff
from stylish.stylish import stringify
from plain.plain import plain
from gendiff.convertors.json import convert as convert2_json
from gendiff.convertors.yaml import convert as convert2_yaml


def main():
    parser = argparse.ArgumentParser(description='Compares\
 two configuration files and shows a difference.')

    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', help='\nset format of output')

    args = parser.parse_args()

    if args.first_file[-4:] == 'json':
        file1 = convert2_json(args.first_file)
    else:
        file1 = convert2_yaml(args.first_file)

    if args.second_file[-4:] == 'json':
        file2 = convert2_json(args.second_file)
    else:
        file2 = convert2_yaml(args.second_file)

    diff_tree = generate_diff(file1, file2)

    if args.format is None:
        print(stringify(diff_tree))
    elif args.format == 'plain':
        print(plain(diff_tree))


if __name__ == '__main__':
    main()
