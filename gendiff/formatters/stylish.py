from itertools import chain


INDENT = '    '

ADDED = '  + '
REMOVED = '  - '
UNCHANGED = '    '
UPDATED = '  - '


def to_str(value):
    """
    Convert values:
    False -> false, True -> true, None -> null
    """
    if value is None:
        return 'null'
    elif isinstance(value, bool):
        return str(value).lower()
    return str(value)


def stylish(tree):

    def iter_(node, depth):

        if not isinstance(node, dict):
            return to_str(node)

        current_indent = INDENT * depth
        lines = []
        for key, value in node.items():
            if not isinstance(value, dict):
                lines.append(f'{current_indent}{INDENT}{key}: {to_str(value)}')

            elif value.get('type') == 'nested':
                children = value.get('children')
                lines.append(f'{current_indent}{INDENT}{key}: {iter_(children, depth + 1)}')

            elif value.get('type') == 'added':
                val = value.get('value')
                lines.append(f'{current_indent}{ADDED}{key}: {iter_(val, depth + 1)}')

            elif value.get('type') == 'unchanged':
                val = value.get('value')
                lines.append(f'{current_indent}{UNCHANGED}{key}: {iter_(val, depth + 1)}')

            elif value.get('type') == 'removed':
                val = value.get('value')
                lines.append(f'{current_indent}{REMOVED}{key}: {iter_(val, depth + 1)}')

            elif value.get('type') == 'updated':
                old_val = value.get('value')
                new_val = value.get('changed_value')
                lines.append(f'{current_indent}{REMOVED}{key}: {iter_(old_val, depth + 1)}')
                lines.append(f'{current_indent}{ADDED}{key}: {iter_(new_val, depth + 1)}')

            else:
                lines.append(f'{current_indent}{INDENT}{key}: {iter_(value, depth + 1)}')

        result = chain("{", lines, [current_indent + "}"])
        return '\n'.join(result)

    return iter_(tree, 0)
