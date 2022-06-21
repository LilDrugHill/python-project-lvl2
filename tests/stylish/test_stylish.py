from formatters.stylish import stringify
from gendiff.comparator import comparator
from gendiff.input_files_parser import parse_input_format


def test_simple_stylish():
    output_fixture = 'tests/fixtures/outputs/stylish_simple.txt'

    with open(output_fixture, encoding='utf-8') as read_file:
        expected_string = read_file.read()

    file1_path = 'tests/fixtures/simple_files/file1.yaml'
    file2_path = 'tests/fixtures/simple_files/file2.yaml'
    file1, file2 = parse_input_format(file1_path, file2_path)
    data = comparator(file1, file2)

    assert stringify(data) == expected_string


def test_deep_stylish():
    output_fixture = 'tests/fixtures/outputs/stylish_deep.txt'

    with open(output_fixture, encoding='utf-8') as read_file:
        expected_string = read_file.read()

    file1_path = 'tests/fixtures/deep_files/file1.yml'
    file2_path = 'tests/fixtures/deep_files/file2.yml'
    file1, file2 = parse_input_format(file1_path, file2_path)
    data = comparator(file1, file2)

    assert stringify(data) == expected_string
