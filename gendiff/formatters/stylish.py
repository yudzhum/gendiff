from itertools import chain


# Intends with status of values
INDENT = '    '
ADDED = '  + '
REMOVED = '  - '


# Statuses of nodes and values
STATUS = {
    'added': ADDED,
    'removed': REMOVED,
    'unchanged': INDENT,
    'nothing': INDENT,
    'nested': INDENT
}


def to_str(value):
    """
    Convert values:
    False -> false, True -> true, None -> null,
    all -> string
    """
    if value is None:
        return 'null'
    elif isinstance(value, bool):
        return str(value).lower()
    return str(value)


def stylish(tree):
    """Take diff tree and return formatted string"""

    def iter_(node, depth):

        # Case of primitive value
        if not isinstance(node, dict):
            return to_str(node)

        cur_indent = INDENT * depth
        lines = []
        for key, value in node.items():
            # Case of primitive value
            if not isinstance(value, dict):
                lines.append(f'{cur_indent}{INDENT}{key}: {to_str(value)}')

            elif value.get('type') == 'updated':
                old_val = value.get('value')
                new_val = value.get('changed_value')
                lines.append(
                    f'{cur_indent}{REMOVED}{key}: {iter_(old_val, depth + 1)}'
                )
                lines.append(
                    f'{cur_indent}{ADDED}{key}: {iter_(new_val, depth + 1)}'
                )

            # Case of types: nested, added, unchanged, removed
            # and dict_value
            else:
                status = value.get('type', 'nothing')
                deep_level = {
                    'nested': value.get('children'),
                    'nothing': value,
                }
                val = deep_level.get(status, value.get('value'))
                lines.append(
                    f'{cur_indent}{STATUS[status]}'
                    f'{key}: {iter_(val, depth + 1)}'
                )

        result = chain("{", lines, [cur_indent + "}"])
        return '\n'.join(result)

    return iter_(tree, 0)
