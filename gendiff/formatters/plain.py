def plain(tree):
    return walk(tree)


def walk(node, path='', key=None):
    if node.get("action"):
        return build_line(node, path, key)

    if key:
        path += f"{key}."

    children = node.keys()

    data = list(
        filter(
            lambda unit: unit is not None,
            map(lambda child: walk(node.get(child), path, child), children),
        )
    )

    return "\n".join(data)


def build_line(node, path, key):

    value1 = to_str(node.get("node1"))
    value2 = to_str(node.get("node2"))
    action = node.get("action")
    path += f"{key}"
    if action == 'add':
        return f"Property '{path}' was added with value: {value2}"
    if action == 'remove':
        return f"Property '{path}' was removed"
    if action == 'changed':
        return f"Property '{path}' was updated. From {value1} to {value2}"
    if action == 'nested':
        return None
    raise KeyError(f'Action "{action}" does not exist')


def to_str(value):
    match value:
        case dict():
            return "[complex value]"
        case bool():
            return str(value).lower()
        case None:
            return 'null'
        case int() | float():
            return value
    return f"'{value}'"
