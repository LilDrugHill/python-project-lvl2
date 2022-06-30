def change_structure(value):

    def walk(node, key=0):

        if node.get('action'):
            return build_leaf(node, key)

        if not node.get('action'):
            children = node.keys()

        children = list(map(lambda child: walk(node.get(child), child), children))

        new_children = {}
        for child in children:
            new_children.update(child)

        if key != 0:
            return {key: new_children}

        return new_children

    return walk(value, 0)


def build_leaf(node, key):
    value1 = node.get('node1')
    value2 = node.get('node2')
    action = node.get('action')
    if action == 'add':
        return {f'+{key}': value2}
    elif action == 'remove':
        return {f'-{key}': value1}
    elif action == 'changed':
        return {f'-{key}': value1, f'+{key}': value2}
    return {f'{key}': value1}


REPLACER = ' '
SPACE_COUNT = 4


def stringify(value):

    def walk(node, depth, path):

        if isinstance(node, tuple) and not isinstance(node[1], dict):
            return REPLACER * SPACE_COUNT * depth + f'{node[0]}: {node[1]}'

        path = ''

        if isinstance(node, dict):
            children = node.items()

        else:
            path += REPLACER * SPACE_COUNT * depth + node[0] + ': '
            children = node[1].items()

        string_node = str(list(map(lambda child: walk(child, depth + 1, path), children)))

        return path + string_node + f'{depth}'

    if isinstance(value, dict):
        return visual(walk(change_structure(value), 0, ''))

    return str(value)


def visual(value):
    index = 0
    while index < len(value):

        if value[index] == ']':
            seporator_position = value[index + 1]
            value = value.replace(
                f']{seporator_position}',
                (f'\n{REPLACER * SPACE_COUNT * int(seporator_position)}' + '}'))
            index = 0
            continue

        index += 1

    return to_str(value)


def to_str(data):

    completed_str = (data
                     .replace('True', 'true')
                     .replace('None', 'null')
                     .replace('False', 'false')
                     .replace('[', '{\n')
                     .replace(', ', '\n')
                     .replace("'", '')
                     .replace('"', '')
                     .replace('\\', '')
                     .replace('  +', '+ ')
                     .replace('  -', '- '))

    return completed_str
