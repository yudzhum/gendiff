ADDED = 'added'
UPDATED = 'updated'
UNCHANGED = 'unchanged'


def get_value(node):
    return node.get('value')


def get_changed_value(node):
    return node.get('changed_value')


def convert_(value):
    result = value
    if isinstance(value, dict):
        result = '[complex value]'
    elif isinstance(value, str):
        result = f"'{value}'"
    elif isinstance(value, bool):
        result = str(value).lower()
    elif value is None:
        result = 'null'
    return result


def get_name(node):
    if isinstance(node, list):
        return ''
    return node.get('name')


def get_type(node):
    return node.get('type')


def get_children(node):
    if isinstance(node, list):
        return node
    return node.get('children')


def is_leaf(node):
    if isinstance(node, list):
        return False
    if get_children(node):
        return False
    return True


def get_values_info(node):
    type = get_type(node)
    result = ''
    if type == ADDED:
        result = f' with value: {convert_(get_value(node))}'
    if type == UPDATED:
        result = (
            f'. From {convert_(get_value(node))} '
            f'to {convert_(get_changed_value(node))}'
        )
    return result


def concate(path, name):
    """Remove blancks and concate path with dots"""

    new_path = f'{path}.{name}'
    return '.'.join(filter(lambda x: x, new_path.split('.')))


def gen_string(node, path):
    """Take node and return info as string"""

    # If node was unchanged it will not show in diff
    type = get_type(node)
    if type == UNCHANGED:
        return None

    # Return info about node
    name = get_name(node)
    new_path = concate(path, name)
    values_info = get_values_info(node)
    string = f"Property '{new_path}' was {type}{values_info}"
    return string


def style_to_plain(node, path=''):
    """Take diff tree and return diff in plain style"""

    # Handle node without children
    if is_leaf(node):
        string = gen_string(node, path)
        return string

    # Handle node with children or children
    children = get_children(node)
    name = get_name(node)
    new_path = f'{path}.{name}'

    result = list(filter(
        lambda x: x, map(lambda x: style_to_plain(x, new_path), children)
    ))
    return '\n'.join(result)
