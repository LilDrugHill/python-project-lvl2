from formatters.stylish import stringify
from gendiff.comparator import comparator
from gendiff.yaml_convertor import convert as convert2_yaml


def test_simple_stylish():
    output_fixture = 'tests/fixtures/outputs/stylish_simple.txt'

    with open(output_fixture, encoding='utf-8') as read_file:
        expected_string = read_file.read()

    file1 = 'tests/fixtures/simple_files/file1.yaml'
    file2 = 'tests/fixtures/simple_files/file2.yaml'
    data = comparator(convert2_yaml(file1), convert2_yaml(file2))

    assert stringify(data) == expected_string


def test_deep_stylish():
    output_fixture = 'tests/fixtures/outputs/stylish_deep.txt'

    with open(output_fixture, encoding='utf-8') as read_file:
        expected_string = read_file.read()

    file1 = 'tests/fixtures/deep_files/file1.yml'
    file2 = 'tests/fixtures/deep_files/file2.yml'
    data = comparator(convert2_yaml(file1), convert2_yaml(file2))

    assert stringify(data) == expected_string
