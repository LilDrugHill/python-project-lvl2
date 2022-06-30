import json
import pytest
from gendiff.gendiff import generate_diff
from gendiff.comparator import build_diff_tree, pair_gen
from gendiff.formatters.json_format import json_format
from gendiff.formatters.plain import plain
from gendiff.formatters.stylish import stringify
from gendiff.input_parser import get_data


expected_res_simple = {'follow': {'action': 'remove', 'node1': False},
                       'host': {'action': 'nested', 'node1': 'hexlet.io'},
                       'proxy': {'action': 'remove', 'node1': '123.234.53.22'},
                       'timeout': {'action': 'changed', 'node1': 50, 'node2': 20},
                       'verbose': {'action': 'add', 'node2': True}}

expected_res_deep = {'common': {'follow': {'action': 'add', 'node2': False},
                                'setting1': {'action': 'nested', 'node1': 'Value 1'},
                                'setting2': {'action': 'remove', 'node1': 200},
                                'setting3': {'action': 'changed', 'node1': True, 'node2': None},
                                'setting4': {'action': 'add', 'node2': 'blah blah'},
                                'setting5': {'action': 'add', 'node2': {'key5': 'value5'}},
                                'setting6': {'doge': {'wow': {'action': 'changed',
                                                              'node1': '',
                                                              'node2': 'so much'}},
                                             'key': {'action': 'nested', 'node1': 'value'},
                                             'ops': {'action': 'add', 'node2': 'vops'}}},
                     'group1': {'baz': {'action': 'changed', 'node1': 'bas', 'node2': 'bars'},
                                'foo': {'action': 'nested', 'node1': 'bar'},
                                'nest': {'action': 'changed',
                                         'node1': {'key': 'value'},
                                         'node2': 'str'}},
                     'group2': {'action': 'remove', 'node1': {'abc': 12345, 'deep': {'id': 45}}},
                     'group3': {'action': 'add',
                                'node2': {'deep': {'id': {'number': 45}}, 'fee': 100500}}}


@pytest.mark.parametrize("file_path1,file_path2,expected",
                         [('tests/fixtures/deep_files/file1.json',
                           'tests/fixtures/deep_files/file2.json',
                           expected_res_deep),
                          ('tests/fixtures/simple_files/file1.json',
                           'tests/fixtures/simple_files/file2.json',
                           expected_res_simple)])
def test_build_diff_tree(file_path1, file_path2, expected):
    file1, file2 = get_data(file_path1), get_data(file_path2)
    assert build_diff_tree(file1, file2) == expected


@pytest.mark.parametrize("value1,value2,key,expected",
                         [(False, '&', 'follow', {'follow': {'action': 'remove', 'node1': False}}),
                          ('&', True, 'verbose', {'verbose': {'action': 'add', 'node2': True}}),
                          (50, 20, 'timeout', {'timeout': {'action': 'changed',
                                                           'node1': 50,
                                                           'node2': 20}}),
                          ('hexlet.io', 'hexlet.io', 'host', {'host': {'action': 'nested',
                                                                       'node1': 'hexlet.io'}})])
def test_pair_gen(value1, value2, key, expected):
    assert pair_gen(value1, value2, key) == expected


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

    data1, data2 = get_data(input1), get_data(input2)

    assert formater(build_diff_tree(data1, data2)) == output


#  Вы имели ввиду единственный тест как ниже?
@pytest.mark.parametrize("input1,input2,output_format,output",
                         [('tests/fixtures/deep_files/file1.yml',
                           'tests/fixtures/deep_files/file2.yml',
                           None,
                           'tests/fixtures/outputs/stylish_deep.txt'),
                          ('tests/fixtures/deep_files/file1.json',
                           'tests/fixtures/deep_files/file2.json',
                           'plain',
                           'tests/fixtures/outputs/plain_deep.txt'),
                          ('tests/fixtures/deep_files/file1.json',
                           'tests/fixtures/deep_files/file2.json',
                           'json',
                           'tests/fixtures/outputs/deep_file.json')])
def test_gendiff(input1, input2, output_format, output):
    if output_format == 'json':
        with open(output, encoding='utf-8') as read_file:
            read_file = json.load(read_file)
            output = json.dumps(read_file, indent=4)
    else:
        with open(output, encoding='utf-8') as read_file:
            output = read_file.read()
    assert generate_diff(input1, input2, output_format) == output
