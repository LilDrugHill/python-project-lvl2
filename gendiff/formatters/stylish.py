REPLACER = ' '
SPACE_COUNT = 4


def stringify(value):

    if isinstance(value, dict):
        return visual(walk(value, 0, ''))

    return str(value)


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
