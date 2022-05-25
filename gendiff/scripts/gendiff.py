#!/usr/bin/env python

import argparse
from gendiff.comparator import generate_diff
from gendiff.converstors.json_conv import convert_json
from gendiff.converstors.yaml_conv import convert_yaml


def main():
    parser = argparse.ArgumentParser(description='Compares\
 two configuration files and shows a difference.')

    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', help='\nset format of output')

    args = parser.parse_args()

    if args.format == 'json':
        file1 = convert_json(args.first_file)
        file2 = convert_json(args.second_file)

    if args.format == 'yaml':
        file1 = convert_yaml(args.first_file)
        file2 = convert_yaml(args.second_file)

    print(generate_diff(file1, file2))


if __name__ == '__main__':
    main()
