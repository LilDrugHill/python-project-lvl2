from formatters.plain import plain
from gendiff.comparator import generate_diff
from gendiff.json_convertor import convert as convert2_json


def test_simple_plain():
    expected_string = "Property 'follow' was removed\n\
Property 'proxy' was removed\n\
Property 'timeout' was updated. From '50' to '20'\n\
Property 'verbose' was added with value: true"

    file1 = 'tests/fixtures/simple_files/file1.json'
    file2 = 'tests/fixtures/simple_files/file2.json'
    data = generate_diff(convert2_json(file1), convert2_json(file2))

    assert plain(data) == expected_string


def test_deep_plain():
    expected_string = "Property 'common.follow' was added with value: false\n\
Property 'common.setting2' was removed\n\
Property 'common.setting3' was updated. From true to null\n\
Property 'common.setting4' was added with value: 'blah blah'\n\
Property 'common.setting5' was added with value: [complex value]\n\
Property 'common.setting6.doge.wow' was updated. From '' to 'so much'\n\
Property 'common.setting6.ops' was added with value: 'vops'\n\
Property 'group1.baz' was updated. From 'bas' to 'bars'\n\
Property 'group1.nest' was updated. From [complex value] to 'str'\n\
Property 'group2' was removed\n\
Property 'group3' was added with value: [complex value]"

    file1 = 'tests/fixtures/deep_files/file1.json'
    file2 = 'tests/fixtures/deep_files/file2.json'
    data = generate_diff(convert2_json(file1), convert2_json(file2))

    assert plain(data) == expected_string
