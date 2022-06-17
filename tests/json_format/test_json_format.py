import json
from gendiff.comparator import generate_diff
from formatters.json_format import json_format
from gendiff.json_convertor import convert as convert2_json


def test_json_format_deep():
    expected_data = 'tests/fixtures/json_output/deep_file.json'

    with open(expected_data, encoding='utf-8') as read_file:
        read_file = json.load(read_file)
        expected_data = json.dumps(read_file, indent=4)

    file1 = 'tests/fixtures/deep_files/file1.json'
    file2 = 'tests/fixtures/deep_files/file2.json'
    data = generate_diff(convert2_json(file1), convert2_json(file2))

    assert json_format(data) == expected_data
