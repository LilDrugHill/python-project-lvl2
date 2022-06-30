from gendiff.input_parser import get_data
from gendiff.formatter import format as format_output
from gendiff.comparator import build_diff_tree


def generate_diff(file_path1, file_path2, format=None):

    data1, data2 = get_data(file_path1), get_data(file_path2)

    return format_output(build_diff_tree(data1, data2), format)
