def plain(tree):

    def walk(node, path):
        print(node)
        if all(isinstance(node, tuple),
               (node[0][0] == '+' or node[0][0] == '-' or node[0][0] == ' ' or len(node) == 3)):
            return gen_string_2visual(node, path)

        if isinstance(node, dict):
            children = list(node.items())

        else:
            path += f'{node[0]}.'
            children = list(node[1].items())

        children = change_2visual(children)

        data = str(list(map(lambda child: walk(child, path), children)))

        return data

    return visual(walk(tree, ''))


def gen_string_2visual(node, path):
    key = node[0]
    value1 = node[1]

    if isinstance(value1, dict):
        value1 = '(complex value)'

    if len(node) == 3 and isinstance(node[2], dict):
        value2 = '(complex value)'
        path += f'{key}'
        return f"Property *{path}* was updated. From *{value1}* to *{value2}*"
    elif len(node) == 3 and not isinstance(node[2], dict):
        value2 = node[2]
        return f"Property *{path}* was updated. From *{value1}* to *{value2}*"

    if key[0] == '+':
        path += f'{key[2:]}'
        return f"Property *{path}* was added with value: *{value1}*"
    elif key[0] == '-':
        path += f'{key[2:]}'
        return f"Property *{path}* was removed"
    else:
        return '&'


def change_2visual(children):
    children.append(('&', '&'))

    for child1, child2 in zip(children, children[1:]):
        if all(child1[0][2:] == child2[0][2:],
               (child1[0][0] == '-' or child1[0][0] == '+'),
               child1[1] != child2[1]):
            key = child1[0][2:]
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


def visual(data):
    changed_data = data.replace('True', 'true')
    changed_data = changed_data.replace('None', 'null')
    changed_data = changed_data.replace('False', 'false')

    changed_data = changed_data.replace('[', '').replace(']', '')
    changed_data = changed_data.replace("'", '').replace('"', '')
    changed_data = changed_data.replace('*', "'").replace(', ', '\n')
    changed_data = changed_data.replace("'(", '[').replace(")'", ']')
    changed_data = changed_data.replace('\\', '').replace('&\n', '')

    return changed_data
