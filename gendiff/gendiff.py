from gendiff.parser import get_data
from gendiff.formatters import format_
from gendiff.comparator import build_diff_tree


def generate_diff(file_path1, file_path2, output_format='stylish'):

    data1, data2 = get_data(file_path1), get_data(file_path2)

    return format_(build_diff_tree(data1, data2), output_format)
