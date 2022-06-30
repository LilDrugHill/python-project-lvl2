import pytest
from gendiff.input_parser import get_data


@pytest.mark.parametrize("fixture_path,expected",
                         [('tests/fixtures/simple_files/file1.json',
                           {'follow': False,
                            'host': 'hexlet.io',
                            'proxy': '123.234.53.22',
                            'timeout': 50}),
                          ('tests/fixtures/simple_files/file2.json',
                           {'host': 'hexlet.io', 'timeout': 20, 'verbose': True}),
                          ('tests/fixtures/simple_files/file1.yaml',
                           {'follow': False,
                            'host': 'hexlet.io',
                            'proxy': '123.234.53.22',
                            'timeout': 50}),
                          ('tests/fixtures/simple_files/file2.yaml',
                           {'host': 'hexlet.io', 'timeout': 20, 'verbose': True})])
def test_input_parser(fixture_path, expected):
    assert get_data(fixture_path) == expected
