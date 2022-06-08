def stringify(value, replacer=' ', spaces_count=4):
    def walk(node, depth, path):

        if isinstance(node, tuple) and not isinstance(node[1], dict):
            return replacer * spaces_count * depth + f'{node[0]}: {node[1]}'

        path = ''

        if isinstance(node, dict):
            children = node.items()

        else:
            path += replacer * spaces_count * depth + node[0] + ': '
            children = node[1].items()

        string_node = str(list(map(lambda child: walk(child, depth + 1, path), children)))

        return path + string_node + f'{depth}'

    if isinstance(value, str):
        return str(value)

    elif isinstance(value, dict):
        return visual(walk(value, 0, ''), replacer, spaces_count)

    else:
        return str(value)


def visual(value, replacer, spaces_count):
    index = 0
    while index < len(value):

        if value[index] == ']':
            seporator_position = value[index + 1]
            value = value.replace(
                f']{seporator_position}',
                (f'\n{replacer * spaces_count * int(seporator_position)}' + '}'))
            index = 0
            continue

        index += 1

    value = value.replace('True', 'true')
    value = value.replace('None', 'null')
    value = value.replace('False', 'false')

    value = value.replace('[', '{\n').replace(', ', '\n')
    value = value.replace("'", '').replace('"', '')
    value = value.replace('\\', '')

    return value
