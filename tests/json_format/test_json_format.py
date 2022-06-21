import json
from gendiff.comparator import comparator
from formatters.json_format import json_format
from gendiff.input_files_parser import parse_input_format


def test_json_format_deep():
    fixture = 'tests/fixtures/outputs/deep_file.json'

    with open(fixture, encoding='utf-8') as read_file:
        read_file = json.load(read_file)
        expected_data = json.dumps(read_file, indent=4)

    file1_path = 'tests/fixtures/deep_files/file1.json'
    file2_path = 'tests/fixtures/deep_files/file2.json'
    file1, file2 = parse_input_format(file1_path, file2_path)
    data = comparator(file1, file2)

    assert json_format(data) == expected_data
