#!/usr/bin/env python

from gendiff.cli import parse
from gendiff.input_parser import read_file
from gendiff.comparator import build_diff_tree
from gendiff.formatters.formatter import format


def main():
    args = parse()

    file1, file2 = read_file(args.first_file), read_file(args.second_file)

    diff_tree = build_diff_tree(file1, file2)
    print(diff_tree)
    print(format(args.format, diff_tree))


if __name__ == '__main__':
    main()
