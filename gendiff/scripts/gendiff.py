#!/usr/bin/env python

from gendiff.arg_parser import parse
from gendiff.input_files_parser import parse_input_format
from gendiff.comparator import generate_diff
from formatters.formatter import change_format as output_format


def main():

    args = parse()

    print(generate_diff(args, args.first_file, args.second_file))


if __name__ == '__main__':
    main()
