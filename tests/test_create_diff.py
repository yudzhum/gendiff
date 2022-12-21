import os
import pytest

from gendiff.create_diff import generate_diff


def get_fixture_path(file_name):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(current_dir, 'fixtures', file_name)


def read(file_path):
    with open(file_path, 'r') as f:
        result = f.read()
    return result



# expected result
plain_data = read(get_fixture_path('plain.txt'))
print(plain_data)  





# Namespace(first_file='file1.json', format=None, second_file='file2.json')
