#!/usr/bin/env python

from gendiff.cli import parse
from gendiff.input_parser import get_data
from gendiff.comparator import build_diff_tree
from gendiff.formatter import format


def main():
    args = parse()

    file1, file2 = get_data(args.first_file), get_data(args.second_file)

    diff_tree = build_diff_tree(file1, file2)
    print(diff_tree)
    print(format(diff_tree, args.format))


if __name__ == '__main__':
    main()
