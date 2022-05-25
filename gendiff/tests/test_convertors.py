from gendiff.converstors.json_conv import convert_json
from gendiff.converstors.yaml_conv import convert_yaml


def test_convert_json():
    res1 = {'follow': False, 'host': 'hexlet.io', 'proxy': '123.234.53.22', 'timeout': 50}
    res2 = {'host': 'hexlet.io', 'timeout': 20, 'verbose': True}

    assert convert_json('gendiff/tests/fixtures/file1.json') == res1
    assert convert_json('gendiff/tests/fixtures/file2.json') == res2


def test_convert_yaml():
    res1 = {'follow': False, 'host': 'hexlet.io', 'proxy': '123.234.53.22', 'timeout': 50}
    res2 = {'host': 'hexlet.io', 'timeout': 20, 'verbose': True}

    assert convert_yaml('gendiff/tests/fixtures/file1.yaml') == res1
    assert convert_yaml('gendiff/tests/fixtures/file2.yaml') == res2
