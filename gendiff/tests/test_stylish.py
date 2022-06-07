from gendiff.stylish import stringify
from gendiff.comparator import generate_diff
from gendiff.convertors.yaml import convert as convert2_yaml


def test_simple_stylish():
    expected_string = '{\n  - follow: false\n    host: hexlet.io\n  - proxy: \
123.234.53.22\n  - timeout: 50\n  + timeout: 20\n  + verbose: true\n}'

    file1 = 'gendiff/tests/fixtures/simple_files/file1.yaml'
    file2 = 'gendiff/tests/fixtures/simple_files/file2.yaml'
    data = generate_diff(convert2_yaml(file1), convert2_yaml(file2))

    assert stringify(data) == expected_string


def test_deep_stylish():
    expected_string = '{\n    common: {\n      + follow: false\n        setting1: Value 1\n\
      - setting2: 200\n      - setting3: true\n      + setting3: null\n\
      + setting4: blah blah\n      + setting5: {\n            key5: value5\n\
        }\n        setting6: {\n            doge: {\n              - wow: \n\
              + wow: so much\n            }\n            key: value\n\
          + ops: vops\n        }\n    }\n    group1: {\n      - baz: bas\n\
      + baz: bars\n        foo: bar\n      - nest: {\n            key: value\n\
        }\n      + nest: str\n    }\n  - group2: {\n        abc: 12345\n\
        deep: {\n            id: 45\n        }\n    }\n  + group3: {\n\
        deep: {\n            id: {\n                number: 45\n\
            }\n        }\n        fee: 100500\n    }\n}'

    file1 = 'gendiff/tests/fixtures/deep_files/file1.yaml'
    file2 = 'gendiff/tests/fixtures/deep_files/file2.yaml'
    data = generate_diff(convert2_yaml(file1), convert2_yaml(file2))

    assert stringify(data) == expected_string