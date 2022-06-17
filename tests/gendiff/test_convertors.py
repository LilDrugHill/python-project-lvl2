import pytest
from gendiff.json_convertor import convert as convert2_json
from gendiff.yaml_convertor import convert as convert2_yaml

res1 = {'follow': False, 'host': 'hexlet.io', 'proxy': '123.234.53.22', 'timeout': 50}
res2 = {'host': 'hexlet.io', 'timeout': 20, 'verbose': True}

path_json1 = 'tests/fixtures/simple_files/file1.json'
path_json2 = 'tests/fixtures/simple_files/file2.json'

path_ymal1 = 'tests/fixtures/simple_files/file1.yaml'
path_yaml2 = 'tests/fixtures/simple_files/file2.yaml'


@pytest.mark.parametrize("fixture_path,expected", [(path_json1, res1), (path_json2, res2)])
def test_convert_json(fixture_path, expected):
    assert convert2_json(fixture_path) == expected


@pytest.mark.parametrize("fixture_path,expected", [(path_ymal1, res1), (path_yaml2, res2)])
def test_convert_yaml(fixture_path, expected):
    assert convert2_yaml(fixture_path) == expected
