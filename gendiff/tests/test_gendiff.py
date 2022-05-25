from gendiff import gendiff


def test_gendiff_simple():
    res = '{\n  - follow: False\n    host: hexlet.io\n  - proxy: \
123.234.53.22\n  - timeout: 50\n  + timeout: 20\n  + verbose: True\n}'

    file1 = 'gendiff/tests/fixtures/file1.json'
    file2 = 'gendiff/tests/fixtures/file2.json'
    assert gendiff.generate_diff(file1, file2) == res
