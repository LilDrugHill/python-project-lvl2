import json
import pytest
from gendiff.formatters.json_format import json_format
from gendiff.formatters.plain import plain
from gendiff.formatters.stylish import stringify
from gendiff.comparator import build_diff_tree
from gendiff.input_parser import read_file as read_file_formated


@pytest.mark.parametrize("formater,input1,input2,output",
                         [(stringify,
                           'tests/fixtures/simple_files/file1.yaml',
                           'tests/fixtures/simple_files/file2.yaml',
                           'tests/fixtures/outputs/stylish_simple.txt'),
                          (stringify,
                           'tests/fixtures/deep_files/file1.yml',
                           'tests/fixtures/deep_files/file2.yml',
                           'tests/fixtures/outputs/stylish_deep.txt'),
                          (plain,
                           'tests/fixtures/simple_files/file1.json',
                           'tests/fixtures/simple_files/file2.json',
                           'tests/fixtures/outputs/plain_simple.txt'),
                          (plain,
                           'tests/fixtures/deep_files/file1.json',
                           'tests/fixtures/deep_files/file2.json',
                           'tests/fixtures/outputs/plain_deep.txt'),
                          (json_format,
                           'tests/fixtures/deep_files/file1.json',
                           'tests/fixtures/deep_files/file2.json',
                           'tests/fixtures/outputs/deep_file.json')])
def test_formatters(formater, input1, input2, output):
    if formater is json_format:
        with open(output, encoding='utf-8') as read_file:
            read_file = json.load(read_file)
            output = json.dumps(read_file, indent=4)
    else:
        with open(output, encoding='utf-8') as read_file:
            output = read_file.read()

    data1, data2 = read_file_formated(input1), read_file_formated(input2)

    assert formater(build_diff_tree(data1, data2)) == output
