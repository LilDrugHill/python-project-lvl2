from gendiff.input_parser import read_file
from gendiff.formatters.formatter import format as format_output
from gendiff.comparator import build_diff_tree


def generate_diff(file_path1, file_path2, format=None):

    data1, data2 = read_file(file_path1), read_file(file_path2)

    return format_output(format, build_diff_tree(data1, data2))
