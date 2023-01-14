def to_str(value):
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


def style_to_plain(tree):

    lines = []
    path = []

    def iter_(node, path):

        for key, value in node.items():

            if value.get('type') == 'nested':
                new_path = path + [key]
                children = value.get('children')
                iter_(children, new_path)

            elif value.get('type') == 'added':
                val = value.get('value')
                new_path = path + [key]
                lines.append(f"Property '{'.'.join(new_path)}' was added with value: {to_str(val)}")

            elif value.get('type') == 'removed':
                new_path = path + [key]
                lines.append(f"Property '{'.'.join(new_path)}' was removed")

            elif value.get('type') == 'updated':
                new_path = path + [key]
                old_val = value.get('value')
                new_val = value.get('changed_value')
                lines.append(f"Property '{'.'.join(new_path)}' was updated. From {to_str(old_val)} to {to_str(new_val)}")

        return '\n'.join(lines)

    return iter_(tree, path)
