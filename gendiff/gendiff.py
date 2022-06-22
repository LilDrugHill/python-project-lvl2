from gendiff.input_output_parser import parse_input
from gendiff.input_output_parser import format as format_output
from gendiff.comparator import comparator


def generate_diff(file_path1, file_path2, format=None):

    file1, file2 = parse_input(file_path1, file_path2)

    return format_output(format, comparator(file1, file2))
