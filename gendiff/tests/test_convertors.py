from gendiff.convertors.json import convert as convert2_json
from gendiff.convertors.yaml import convert as convert2_yaml

res1 = {'follow': False, 'host': 'hexlet.io', 'proxy': '123.234.53.22', 'timeout': 50}
res2 = {'host': 'hexlet.io', 'timeout': 20, 'verbose': True}


def test_convert_json():
    assert convert2_json('gendiff/tests/fixtures/simple_files/file1.json') == res1
    assert convert2_json('gendiff/tests/fixtures/simple_files/file2.json') == res2


def test_convert_yaml():
    assert convert2_yaml('gendiff/tests/fixtures/simple_files/file1.yaml') == res1
    assert convert2_yaml('gendiff/tests/fixtures/simple_files/file2.yaml') == res2
