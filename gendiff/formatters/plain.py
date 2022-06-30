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

        data = str(list(map(lambda child: walk(node.get(child), path, child), children)))

        return data

    return to_str(walk(tree, ''))


def build_string(node, path, key):

    value1 = safe_value_vison(node.get('node1'))
    value2 = safe_value_vison(node.get('node2'))
    action = node.get('action')

    if action == 'add':
        path += f'{key}'
        return f"Property *{path}* was added with value: {value2}"

    elif action == 'remove':
        path += f'{key}'
        return f"Property *{path}* was removed"

    elif action == 'changed':
        path += f'{key}'
        return f"Property *{path}* was updated. From {value1} to {value2}"

    return NOTHING


def to_str(data):
    changed_data = (data
                    .replace('[', '').replace(']', '')
                    .replace('"', '').replace("'", '')
                    .replace(', ', '\n')
                    .replace("(", '[').replace(")", ']')
                    .replace('\\', '').replace("&\n", '')
                    .replace('*', "'")
                    .replace("True", 'true')
                    .replace('None', 'null')
                    .replace("False", 'false'))
    return changed_data


def safe_value_vison(value):
    if isinstance(value, dict):
        value = '(complex value)'

    elif isinstance(value, str):
        value = f"*{value}*"

    return value
