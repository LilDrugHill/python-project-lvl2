from gendiff.input_files_parser import parse_input_format
from formatters.stylish import stringify
from gendiff.comparator import comparator


def generate_diff(file_path1, file_path2):

    file1, file2 = parse_input_format(file_path1, file_path2)

    return stringify(comparator(file1, file2))
