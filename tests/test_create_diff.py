import os
import json
import pytest

from gendiff.create_diff import generate_diff


def get_fixture_path(file_name):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(current_dir, 'fixtures', file_name)


def read(file_path):
    with open(file_path, 'r') as f:
        result = f.read()
    return result


# source data
plain_dict1 = json.load(open(get_fixture_path('file1.json')))
plain_dict2 = json.load(open(get_fixture_path('file2.json')))

# expected result
plain_expected = read(get_fixture_path('plain.txt')) 


def test_plain():
    assert generate_diff(plain_dict1, plain_dict2) == plain_expected