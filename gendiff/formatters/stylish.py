import itertools


SPACE = " "
SPACES_COUNT = 4


def stylish(tree):
    return walk(tree)


def walk(node, depth=0):
    if not isinstance(node, dict):
        return to_str(node)

    deep_indent_size = depth + SPACES_COUNT
    deep_indent = SPACE * deep_indent_size
    current_indent = SPACE * depth
    lines = []
    for key, val in node.items():
        if isinstance(val, dict) and (action := val.get("action")):
            match action:
                case "add":
                    lines.append(
                        f'{(deep_indent_size - 2) * SPACE}+ {key}:\
 {walk(val.get("node2"), deep_indent_size)}'
                    )
                case "remove":
                    lines.append(
                        f'{(deep_indent_size - 2) * SPACE}- {key}:\
 {walk(val.get("node1"), deep_indent_size)}'
                    )
                case "nested":
                    lines.append(
                        f'{(deep_indent_size - 2) * SPACE}  {key}:\
 {walk(val.get("node1"), deep_indent_size)}'
                    )
                case "changed":
                    lines.append(
                        f'{(deep_indent_size - 2) * SPACE}- {key}:\
 {walk(val.get("node1"), deep_indent_size)}'
                    )
                    lines.append(
                        f'{(deep_indent_size - 2) * SPACE}+ {key}:\
 {walk(val.get("node2"), deep_indent_size)}'
                    )
        else:
            lines.append(f"{deep_indent}{key}: {walk(val, deep_indent_size)}")
    some_str = itertools.chain(["{"], lines, [current_indent + "}"])
    return "\n".join(some_str)


def to_str(value):
    if isinstance(value, bool):
        return str(value).lower()
    if value is None:
        return 'null'
    return value
