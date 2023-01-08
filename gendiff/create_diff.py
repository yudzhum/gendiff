from gendiff.formatters.stylish import stylish
from gendiff.formatters.plain import style_to_plain
from gendiff.parse import parse_data
import json


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


def get_formatter(format_name):
    formatter = stylish
    if format_name == 'plain':
        formatter = style_to_plain
    if format_name == 'json':
        formatter = json.dumps
    return formatter


def generate_diff(filepath1, filepath2, format_name='stylish'):
    dict1 = parse_data(filepath1)
    dict2 = parse_data(filepath2)

    diff_tree = generate_diff_tree(dict1, dict2)

    formatter = get_formatter(format_name)
    return formatter(diff_tree)
