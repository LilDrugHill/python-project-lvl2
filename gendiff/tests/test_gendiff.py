from gendiff import comparator
from gendiff.converstors.json_conv import convert_json
from gendiff.converstors.yaml_conv import convert_yaml


def test_gendiff_json():
    res = '{\n  - follow: False\n    host: hexlet.io\n  - proxy: \
123.234.53.22\n  - timeout: 50\n  + timeout: 20\n  + verbose: True\n}'

    file1 = 'gendiff/tests/fixtures/file1.json'
    file2 = 'gendiff/tests/fixtures/file2.json'

    converted_file1 = convert_json(file1)
    converted_file2 = convert_json(file2)

    assert comparator.generate_diff(converted_file1, converted_file2) == res


def test_gendiff_yaml():
    res = '{\n  - follow: False\n    host: hexlet.io\n  - proxy: \
123.234.53.22\n  - timeout: 50\n  + timeout: 20\n  + verbose: True\n}'

    file1 = 'gendiff/tests/fixtures/file1.yaml'
    file2 = 'gendiff/tests/fixtures/file2.yaml'

    converted_file1 = convert_yaml(file1)
    converted_file2 = convert_yaml(file2)

    assert comparator.generate_diff(converted_file1, converted_file2) == res
