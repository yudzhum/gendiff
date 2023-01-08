import os
import json
import pytest

import yaml 
try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper

from gendiff.create_diff import generate_diff
from gendiff.formatters.stylish import stylish
from gendiff.parse import parse_data


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


def test_plain_json():
    diff = generate_diff(plain_json1, plain_json2)
    assert diff == plain_expected


def test_plain_yaml():
    diff = generate_diff(plain_yaml1, plain_yaml2)
    assert diff == plain_expected


def test_nested_json():
    diff = generate_diff(nested_json1, nested_json2)
    assert diff == nested_expected


def test_nested_yaml():
    diff = generate_diff(nested_yaml1, nested_yaml2)
    assert diff == nested_expected
