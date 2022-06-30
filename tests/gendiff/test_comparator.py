import pytest
from gendiff.comparator import build_diff_tree, pair_gen
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
