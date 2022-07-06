from gendiff.formatters.stylish import json_value  # Change None, False, True -> null, false, true


NOTHING = '&'


def plain(tree):

    def walk(node, path, key=None):
        if node.get('action'):
            return build_string(node, path, key)

        if not key:
            children = node.keys()

        else:
            path += f'{key}.'
            children = node.keys()

        data = list(filter(lambda unit: unit is not None, map(lambda child: walk(node.get(child), path, child), children)))

        return '\n'.join(data)

    return walk(tree, '')


def build_string(node, path, key):

    value1 = safe_value_vison(node.get('node1'))
    value2 = safe_value_vison(node.get('node2'))
    action = node.get('action')
    match action:
        case 'add':
            path += f'{key}'
            return f"Property '{path}' was added with value: {value2}"
        case 'remove':
            path += f'{key}'
            return f"Property '{path}' was removed"
        case 'changed':
            path += f'{key}'
            return f"Property '{path}' was updated. From {value1} to {value2}"

    pass


def safe_value_vison(value):
    match value:
        case dict():
            return '[complex value]'
        case str():
            return f"\'{value}\'"
        case _:
            return json_value(value)