import pytest
from gendiff.input_files_parser import parse_input_format


res1 = {'follow': False, 'host': 'hexlet.io', 'proxy': '123.234.53.22', 'timeout': 50}
res2 = {'host': 'hexlet.io', 'timeout': 20, 'verbose': True}

path_json1 = 'tests/fixtures/simple_files/file1.json'
path_json2 = 'tests/fixtures/simple_files/file2.json'
path_yaml1 = 'tests/fixtures/simple_files/file1.yaml'
path_yaml2 = 'tests/fixtures/simple_files/file2.yaml'


@pytest.mark.parametrize("fixture_path1,fixture_path2,expected1,expected2",
                         [(path_json1, path_json2, res1, res2),
                          (path_yaml1, path_yaml2, res1, res2)])
def test_input_parser(fixture_path1, fixture_path2, expected1, expected2):
    assert parse_input_format(fixture_path1, fixture_path2) == (expected1, expected2)
