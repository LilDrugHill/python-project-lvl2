from formatters.plain import plain
from gendiff.comparator import comparator
from gendiff.json_convertor import convert as convert2_json


def test_simple_plain():
    output_fixture = 'tests/fixtures/outputs/palin_simple.txt'

    with open(output_fixture, encoding='utf-8') as read_file:
        expected_string = read_file.read()

    file1 = 'tests/fixtures/simple_files/file1.json'
    file2 = 'tests/fixtures/simple_files/file2.json'
    data = comparator(convert2_json(file1), convert2_json(file2))

    assert plain(data) == expected_string


def test_deep_plain():
    output_fixture = 'tests/fixtures/outputs/plain_deep.txt'

    with open(output_fixture, encoding='utf-8') as read_file:
        expected_string = read_file.read()

    file1 = 'tests/fixtures/deep_files/file1.json'
    file2 = 'tests/fixtures/deep_files/file2.json'
    data = comparator(convert2_json(file1), convert2_json(file2))

    assert plain(data) == expected_string
