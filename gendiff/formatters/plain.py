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

    def iter_(node, path):

        for key, value in node.items():
            new_path = path + [key]

            if value.get('type') == 'nested':
                children = value.get('children')
                iter_(children, new_path)

            else:
                status = value.get('type')
                val = value.get('value')
                new_val = value.get('changed_value')

                strings = {
                    'added': f"Property '{'.'.join(new_path)}' was added "
                    f"with value: {to_str(val)}",
                    'removed': f"Property '{'.'.join(new_path)}' was removed",
                    'unchanged': "",
                    'updated': f"Property '{'.'.join(new_path)}' was updated. "
                    f"From {to_str(val)} to {to_str(new_val)}",
                }
                lines.append(strings[status])

        result = filter(lambda x: x if x != "" else None, lines)
        return '\n'.join(result)

    return iter_(tree, path=[])
