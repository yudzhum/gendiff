from gendiff.formatters.stylish import stylish


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
            node['type'] = 'deleted'
            node['value'] = dict1[key]
        elif dict1[key] == dict2[key]:
            node['type'] = 'unchanged'
            node['value'] = dict1[key]
        else:
            node['type'] = 'changed'
            if isinstance(dict1[key], dict) and isinstance(dict2[key], dict):
                children = generate_diff_tree(dict1[key], dict2[key])
                node['children'] = children
            else:
                node['value'] = dict1[key]
                node['changed_value'] = dict2[key]

        tree.append(node)

    return tree


def generate_diff(dict1, dict2, formatter=stylish):

    diff_tree = generate_diff_tree(dict1, dict2)

    return formatter(diff_tree)
