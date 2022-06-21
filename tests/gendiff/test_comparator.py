import pytest
from gendiff.comparator import comparator, pair_gen, new_tree_gen
from gendiff.input_files_parser import parse_input_format


expected_res_simple = {'-follow': False,
                       '%host': 'hexlet.io',
                       '-proxy': '123.234.53.22',
                       '-timeout': 50, '+timeout': 20,
                       '+verbose': True}

expected_res_deep = {'common': {'+follow': False,
                                '%setting1': 'Value 1',
                                '-setting2': 200,
                                '-setting3': True,
                                '+setting3': None,
                                '+setting4': 'blah blah',
                                '+setting5': {'key5': 'value5'},
                                'setting6': {'doge': {'-wow': '', '+wow': 'so much'},
                                             '%key': 'value', '+ops': 'vops'}},
                     'group1': {'-baz': 'bas',
                                '+baz': 'bars',
                                '%foo': 'bar',
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
def test_comparator(file_path1, file_path2, expected):
    file1, file2 = parse_input_format(file_path1, file_path2)
    assert comparator(file1, file2) == expected


@pytest.mark.parametrize("value1,value2,key,expected",
                         [(False, '&', 'follow', ('-follow', False)),
                          ('&', True, 'verbose', ('+verbose', True)),
                          (50, 20, 'timeout', (('-timeout', 50), ('+timeout', 20))),
                          ('hexlet.io', 'hexlet.io', 'host', ('%host', 'hexlet.io'))])
def test_pair_gen(value1, value2, key, expected):
    assert pair_gen(value1, value2, key) == expected


expected_tree1 = {'-follow': False,
                  '%host': 'hexlet.io',
                  '-proxy': '123.234.53.22',
                  '-timeout': 50,
                  '+timeout': 20,
                  '+verbose': True}

expected_tree2 = (
    'group1',
    {
        '-baz': 'bas',
        '+baz': 'bars',
        '%foo': 'bar',
        '-nest': {'key': 'value'},
        '+nest': 'str'
    }
)

key1 = 0
new_children1 = [('-follow', False),
                 ('%host', 'hexlet.io'),
                 ('-proxy', '123.234.53.22'),
                 (('-timeout', 50), ('+timeout', 20)),
                 ('+verbose', True)]

key2 = 'group1'
new_children2 = [(('-baz', 'bas'), ('+baz', 'bars')),
                 ('%foo', 'bar'),
                 (('-nest', {'key': 'value'}), ('+nest', 'str'))]


@pytest.mark.parametrize("key,new_children,expected",
                         [(key1, new_children1, expected_tree1),
                          (key2, new_children2, expected_tree2)])
def test_new_tree_gen(key, new_children, expected):
    assert new_tree_gen(key, new_children) == expected
