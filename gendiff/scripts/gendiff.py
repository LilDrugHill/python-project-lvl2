#!/usr/bin/env python

from gendiff.cli import parse
from gendiff.input_output_parser import parse_input, format
from gendiff.comparator import comparator


def main():
    args = parse()

    file1, file2 = parse_input(args.first_file), parse_input(args.second_file)

    diff_tree = comparator(file1, file2)

    print(format(args.format, diff_tree))


if __name__ == '__main__':
    main()
