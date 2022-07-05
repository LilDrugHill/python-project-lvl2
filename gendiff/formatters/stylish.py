import itertools


REPLACER = ' '
SPACE_COUNT = 4


def change_structure(value):

    def walk(node, key=0):

        if node.get('action'):
            return build_leaf(node, key)

        children = node.keys()

        children = list(map(lambda child: walk(node.get(child), child), children))

        new_children = {}
        for child in children:
            new_children.update(child)

        if key != 0:
            return {f'{key}': new_children}

        return new_children

    return walk(value, 0)


def build_leaf(node, key):
    value1 = node.get('node1')
    value2 = node.get('node2')
    action = node.get('action')
    match action:
        case 'add':
            return {f'+{key}': value2}
        case 'remove':
            return {f'-{key}': value1}
        case 'changed':
            return {f'-{key}': value1, f'+{key}': value2}
        case 'nested':
            return {f'{key}': value1}


def stringify(value):

    def walk(current_value, depth):
        if not isinstance(current_value, dict):
            return str(current_value)

        deep_indent_size = depth + SPACE_COUNT
        deep_indent = REPLACER * deep_indent_size
        current_indent = REPLACER * depth
        lines = []
        for key, val in current_value.items():
            lines.append(f'{deep_indent}{key}: {walk(val, deep_indent_size)}')
        result = itertools.chain("{", lines, [current_indent + "}"])
        return '\n'.join(result)

    return replace_(walk(change_structure(value), 0))


def replace_(value):
    new_value = (value.replace('False', 'false')
                      .replace('True', 'true')
                      .replace('None', 'null')
                      .replace('  +', '+ ')
                      .replace('  -', '- '))
    return new_value
