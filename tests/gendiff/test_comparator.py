from gendiff.comparator import generate_diff, pair_gen, new_tree_gen
from gendiff.convertors.json import convert as convert2_json
from gendiff.convertors.yaml import convert as convert2_yaml


def test_simple_gendiff_json():
    expected_res = {'-follow': False,
                    '%host': 'hexlet.io',
                    '-proxy': '123.234.53.22',
                    '-timeout': 50, '+timeout': 20,
                    '+verbose': True}

    file1 = 'tests/fixtures/simple_files/file1.json'
    file2 = 'tests/fixtures/simple_files/file2.json'

    converted_file1 = convert2_json(file1)
    converted_file2 = convert2_json(file2)

    assert generate_diff(converted_file1, converted_file2) == expected_res


def test_simple_gendiff_yaml():
    expected_res = {'-follow': False,
                    '%host': 'hexlet.io',
                    '-proxy': '123.234.53.22',
                    '-timeout': 50,
                    '+timeout': 20,
                    '+verbose': True}

    file1 = 'tests/fixtures/simple_files/file1.yaml'
    file2 = 'tests/fixtures/simple_files/file2.yaml'

    converted_file1 = convert2_yaml(file1)
    converted_file2 = convert2_yaml(file2)

    assert generate_diff(converted_file1, converted_file2) == expected_res


def test_depth_gendiff_json():
    expected_res = {'common': {'+follow': False,
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

    file1 = 'tests/fixtures/deep_files/file1.json'
    file2 = 'tests/fixtures/deep_files/file2.json'

    converted_file1 = convert2_json(file1)
    converted_file2 = convert2_json(file2)

    assert generate_diff(converted_file1, converted_file2) == expected_res


def test_depth_gendiff_yaml():
    expected_res = {'common': {'+follow': False,
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

    file1 = 'tests/fixtures/deep_files/file1.yaml'
    file2 = 'tests/fixtures/deep_files/file2.yaml'

    converted_file1 = convert2_yaml(file1)
    converted_file2 = convert2_yaml(file2)

    assert generate_diff(converted_file1, converted_file2) == expected_res


def test_pair_gen():
    expected_res1 = ('-follow', False)
    expected_res2 = ('+verbose', True)
    expected_res3 = (('-timeout', 50), ('+timeout', 20))
    expected_res4 = ('%host', 'hexlet.io')

    assert pair_gen(False, '&', 'follow') == expected_res1
    assert pair_gen('&', True, 'verbose') == expected_res2
    assert pair_gen(50, 20, 'timeout') == expected_res3
    assert pair_gen('hexlet.io', 'hexlet.io', 'host') == expected_res4


def test_new_tree_gen():
    excepted_res1 = {'-follow': False,
                     '%host': 'hexlet.io',
                     '-proxy': '123.234.53.22',
                     '-timeout': 50,
                     '+timeout': 20,
                     '+verbose': True}
    excepted_res2 = (
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

    assert new_tree_gen(key1, new_children1) == excepted_res1
    assert new_tree_gen(key2, new_children2) == excepted_res2
