import os
import pytest

from gendiff.gendiff import generate_diff


def get_fixture_path(file_name):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(current_dir, 'fixtures', file_name)


def read(file_path):
    with open(file_path, 'r') as f:
        result = f.read()
    return result


# source data
plain_json1 = get_fixture_path('file1.json')
plain_json2 = get_fixture_path('file2.json')
plain_yaml1 = get_fixture_path('plain_yaml1.yaml')
plain_yaml2 = get_fixture_path('plain_yaml2.yaml')
nested_json1 = get_fixture_path('nested_file1.json')
nested_json2 = get_fixture_path('nested_file2.json')
nested_yaml1 = get_fixture_path('nested_yaml1.yaml')
nested_yaml2 = get_fixture_path('nested_yaml2.yaml')

# expected result
plain_expected = read(get_fixture_path('plain.txt'))
nested_expected = read(get_fixture_path('nested.txt'))
formatter_plain = read(get_fixture_path('formatter_plain.txt'))
formatter_json = read(get_fixture_path('json_expected.json'))


@pytest.mark.parametrize(
    'file1, file2, expected',
    [(plain_json1, plain_json2, plain_expected),
    (plain_yaml1, plain_yaml2, plain_expected),
    (nested_json1, nested_json2, nested_expected),
    (nested_yaml1, nested_yaml2, nested_expected),
    (nested_json1, nested_yaml2, nested_expected)]
    )

def test_stylish(file1, file2, expected):
    format_name = 'stylish'
    assert generate_diff(file1, file2, format_name) == expected


@pytest.mark.parametrize(
    'file1, file2',
    [(nested_json1, nested_json2),
    (nested_yaml1, nested_yaml2),
    (nested_json1, nested_yaml2)]
    )

def test_formatter_plain(file1, file2):
    format_name = 'plain'
    assert generate_diff(file1, file2, format_name) == formatter_plain


@pytest.mark.parametrize(
    'file1, file2',
    [(nested_json1, nested_json2),
    (nested_yaml1, nested_yaml2),
    (nested_json1, nested_yaml2)]
    )

def test_formatter_json(file1, file2):
    format_name = 'json'
    assert generate_diff(file1, file2, format_name) == formatter_json
