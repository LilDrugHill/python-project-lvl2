#!/usr/bin/env python

from gendiff.arg_parser import ARGS
from gendiff.comparator import generate_diff


def main():

    print(generate_diff(ARGS.first_file, ARGS.second_file))


if __name__ == '__main__':
    main()
