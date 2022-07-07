import os.path
import pytest

from gendiff.gendiff import generate_diff


TESTS_DIR = os.path.dirname('tests/fixtures')
FIXTURES_PATH = f'{TESTS_DIR}/fixtures'


@pytest.mark.parametrize("file1,file2,output_format,output_file",
                         [('file1.yml',
                           'file2.yml',
                           'stylish',
                           'stylish_output.txt'),
                          ('file1.json',
                           'file2.json',
                           'plain',
                           'plain_output.txt')])
def test_gendiff(file1, file2, output_format, output_file):
    file_path1 = os.path.join(FIXTURES_PATH, file1)
    file_path2 = os.path.join(FIXTURES_PATH, file2)
    output_path = os.path.join(FIXTURES_PATH, output_file)
    with open(output_path, encoding='utf-8') as read_file:
        output = read_file.read()
    assert generate_diff(file_path1, file_path2, output_format) == output
