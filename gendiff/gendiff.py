from gendiff.formatters.stylish import stylish
from gendiff.formatters.plain import style_to_plain
from gendiff.formatters.format_json import format_to_json
from gendiff.parse import parse_data
import os


def generate_diff_tree(dict1, dict2):
    """function take 2 dictionatries and return 1 diff tree"""

    merged = dict1.keys() | dict2.keys()
    sorted_merged = sorted(merged)

    tree = []
    for key in sorted_merged:
        node = {}
        node['name'] = key
        if key not in dict1:
            node['type'] = 'added'
            node['value'] = dict2[key]
        elif key not in dict2:
            node['type'] = 'removed'
            node['value'] = dict1[key]
        elif dict1[key] == dict2[key]:
            node['type'] = 'unchanged'
            node['value'] = dict1[key]
        else:
            node['type'] = 'updated'
            if isinstance(dict1[key], dict) and isinstance(dict2[key], dict):
                children = generate_diff_tree(dict1[key], dict2[key])
                node['children'] = children
            else:
                node['value'] = dict1[key]
                node['changed_value'] = dict2[key]

        tree.append(node)

    return tree


def get_format(format_name):
    """
    Return format function
    Choises are stylish, plain, json
    """
    format = stylish
    if format_name == 'plain':
        format = style_to_plain
    if format_name == 'json':
        format = format_to_json
    return format


def get_data(filepath):
    """
    Open file, read data
    Return dict
    """
    root, extension = os.path.splitext(filepath)

    with open(f'{filepath}') as f:
        data = f.read()
        return parse_data(data, extension[1:])


def generate_diff(filepath1, filepath2, format_name='stylish'):
    """
    Take 2 files in formats: json, yaml.
    Return diff in formats stylish, plain and json
    """
    # Open files and return dicitonaries
    dict1 = get_data(filepath1)
    dict2 = get_data(filepath2)

    # Generate diff tree from two dictionaries
    diff_tree = generate_diff_tree(dict1, dict2)

    # Style diff with formatter
    format = get_format(format_name)
    return format(diff_tree)
