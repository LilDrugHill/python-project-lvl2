import pytest
from gendiff.gendiff import generate_diff


FIXTURE_PATH = 'tests/fixtures/deep_files/'
OUTPUT_PATH = 'tests/fixtures/outputs/'


@pytest.mark.parametrize("file1,file2,output_format,output_file",
                         [('file1.yml',
                           'file2.yml',
                           None,
                           'stylish_deep.txt'),
                          ('file1.json',
                           'file2.json',
                           'plain',
                           'plain_deep.txt')])
def test_gendiff(file1, file2, output_format, output_file):
    file_path1 = FIXTURE_PATH + file1
    file_path2 = FIXTURE_PATH + file2
    output_path = OUTPUT_PATH + output_file
    with open(output_path, encoding='utf-8') as read_file:
        output = read_file.read()
    assert generate_diff(file_path1, file_path2, output_format) == output
