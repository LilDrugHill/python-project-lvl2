from gendiff.input_files_parser import parse_input_format
from gendiff.comparator import comparator
from formatters.formatter import choose_format


def generate_diff(file_path1, file_path2, format=None):

    file1, file2 = parse_input_format(file_path1, file_path2)

    return choose_format(format, comparator(file1, file2))
