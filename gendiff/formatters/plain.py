def plain(tree):
    return walk(tree, "")


def walk(node, path, key=None):
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

    value1 = safe_value_vision(node.get("node1"))
    value2 = safe_value_vision(node.get("node2"))
    action = node.get("action")
    match action:
        case "add":
            path += f"{key}"
            return f"Property '{path}' was added with value: {value2}"
        case "remove":
            path += f"{key}"
            return f"Property '{path}' was removed"
        case "changed":
            path += f"{key}"
            return f"Property '{path}' was updated. From {value1} to {value2}"
    return None


def safe_value_vision(value):
    match value:
        case dict():
            return "[complex value]"
        case str():
            return f"'{value}'"
        case _:
            return to_str(value)


def to_str(value):
    if isinstance(value, bool):
        return str(value).lower()
    if value is None:
        return 'null'
    return value
