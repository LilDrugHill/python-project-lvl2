#!/usr/bin/env python

from gendiff.arg_parser import parse
from gendiff.input_files_parser import parse_input_format
from gendiff.comparator import generate_diff
from formatters.formatter import change_format as output_format


def main():
    args = parse()

    file1, file2 = parse_input_format(args)

    diff_tree = generate_diff(file1, file2)

    print(output_format(args, diff_tree))


if __name__ == '__main__':
    main()
