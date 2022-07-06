import itertools


REPLACER = " "
SPACES_COUNT = 4
ADD = "+ "
REMOVE = "- "


def stylish(tree):
    print(tree)

    def walk(node, depth):
        if not isinstance(node, dict):
            return str(json_value(node))

        deep_indent_size = depth + SPACES_COUNT
        deep_indent = REPLACER * deep_indent_size
        current_indent = REPLACER * depth
        lines = []
        for key, val in node.items():
            match get_action(val):
                case "add":
                    lines.append(
                        f'{(deep_indent_size - 2) * REPLACER}+ {key}:\
 {walk(val.get("node2"), deep_indent_size)}'
                    )
                case "remove":
                    lines.append(
                        f'{(deep_indent_size - 2) * REPLACER}- {key}:\
 {walk(val.get("node1"), deep_indent_size)}'
                    )
                case "nested":
                    lines.append(
                        f'{(deep_indent_size - 2) * REPLACER}  {key}:\
 {walk(val.get("node1"), deep_indent_size)}'
                    )
                case "changed":
                    lines.append(
                        f'{(deep_indent_size - 2) * REPLACER}- {key}:\
 {walk(val.get("node1"), deep_indent_size)}'
                    )
                    lines.append(
                        f'{(deep_indent_size - 2) * REPLACER}+ {key}:\
 {walk(val.get("node2"), deep_indent_size)}'
                    )
                case _:
                    lines.append(f"{deep_indent}{key}: {walk(val, deep_indent_size)}")
        some_str = itertools.chain(["{"], lines, [current_indent + "}"])
        return "\n".join(some_str)

    return walk(tree, 0)


def get_action(value):
    return value.get("action") if isinstance(value, dict) else value


def json_value(value):
    match value:
        case False:
            return "false"
        case True:
            return "true"
        case None:
            return "null"
    return value
