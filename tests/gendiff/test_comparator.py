import pytest
from gendiff.comparator import build_diff_tree, pair_gen, new_children_and_values_gen
from gendiff.input_parser import read_file


expected_res_simple = {'-follow': False,
                       'host': 'hexlet.io',
                       '-proxy': '123.234.53.22',
                       '-timeout': 50, '+timeout': 20,
                       '+verbose': True}

expected_res_deep = {'common': {'+follow': False,
                                'setting1': 'Value 1',
                                '-setting2': 200,
                                '-setting3': True,
                                '+setting3': None,
                                '+setting4': 'blah blah',
                                '+setting5': {'key5': 'value5'},
                                'setting6': {'doge': {'-wow': '', '+wow': 'so much'},
                                             'key': 'value', '+ops': 'vops'}},
                     'group1': {'-baz': 'bas',
                                '+baz': 'bars',
                                'foo': 'bar',
                                '-nest': {'key': 'value'},
                                '+nest': 'str'},
                     '-group2': {'abc': 12345, 'deep': {'id': 45}},
                     '+group3': {'deep': {'id': {'number': 45}}, 'fee': 100500}}


@pytest.mark.parametrize("file_path1,file_path2,expected",
                         [('tests/fixtures/deep_files/file1.json',
                           'tests/fixtures/deep_files/file2.json',
                           expected_res_deep),
                          ('tests/fixtures/simple_files/file1.json',
                           'tests/fixtures/simple_files/file2.json',
                           expected_res_simple)])
def test_build_diff_tree(file_path1, file_path2, expected):
    file1, file2 = read_file(file_path1), read_file(file_path2)
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


new_sorted_children1 = ['-follow', 'host', '-proxy', '-timeout', '+timeout', '+verbose']

new_sorted_children2 = ['-baz', '+baz', 'foo', '-nest', '+nest']

new_values1 = [False, 'hexlet.io', '123.234.53.22', 50, 20, True]

new_values2 = ['bas', 'bars', 'bar', {'key': 'value'}, 'str']

new_children1 = [{'follow': {'action': 'remove', 'node1': False}},
                 {'host': {'action': 'nested', 'node1': 'hexlet.io'}},
                 {'proxy': {'action': 'remove', 'node1': '123.234.53.22'}},
                 {'timeout': {'action': 'changed', 'node1': 50, 'node2': 20}},
                 {'verbose': {'action': 'add', 'node2': True}}]

new_children2 = [{'baz': {'action': 'changed', 'node1': 'bas', 'node2': 'bars'}},
                 {'foo': {'action': 'nested', 'node1': 'bar'}},
                 {'nest': {'action': 'changed', 'node1': {'key': 'value'}, 'node2': 'str'}}]


@pytest.mark.parametrize("new_children,new_sorted_children,new_values",
                         [(new_children1, new_sorted_children1, new_values1),
                          (new_children2, new_sorted_children2, new_values2)])
def test_new_children_and_values_gen(new_children, new_sorted_children, new_values):
    assert new_children_and_values_gen(new_children) == (new_sorted_children, new_values)
