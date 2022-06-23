def plain(tree):

    def walk(node, path):

        if (
            isinstance(node, tuple)
            and (
                node[0][0] == '+'
                or node[0][0] == '-'
                or not isinstance(node[1], dict)
                or len(node) == 3
            )
        ):
            return gen_diff_string(node, path)

        if isinstance(node, dict):
            children = list(node.items())

        else:
            path += f'{node[0]}.'
            children = list(node[1].items())

        children = change_children(children)

        data = str(list(map(lambda child: walk(child, path), children)))

        return data

    return to_str(walk(tree, ''))


def gen_diff_string(node, path):
    key = node[0]
    value1 = node[1]

    value1 = safe_value_vison(value1)

    if len(node) == 3 and isinstance(node[2], dict):
        value2 = safe_value_vison(node[2])
        path += f'{key}'
        return f"Property *{path}* was updated. From {value1} to {value2}"
    elif len(node) == 3 and not isinstance(node[2], dict):
        value2 = safe_value_vison(node[2])
        path += f'{key}'
        return f"Property *{path}* was updated. From {value1} to {value2}"

    if key[0] == '+':
        path += f'{key[1:]}'
        return f"Property *{path}* was added with value: {value1}"
    elif key[0] == '-':
        path += f'{key[1:]}'
        return f"Property *{path}* was removed"
    else:
        return '&'


def change_children(children):
    children.append(('&', '&'))

    for child1, child2 in zip(children, children[1:]):
        if (
            child1[0][1:] == child2[0][1:]
            and (child1[0][0] == '-' or child1[0][0] == '+')
            and child1[1] != child2[1]
        ):
            key = child1[0][1:]
            value1 = child1[1]
            value2 = child2[1]
            place = children.index(child1)
            children.pop(place)
            children.pop(place)
            children.insert(place, (key, value1, value2))
            children.insert(0, ('&', '&'))

    while ('&', '&') in children:
        children.remove(('&', '&'))

    return children


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
        value = f'*{value}*'

    return value
