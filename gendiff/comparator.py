EMPTY_VALUE = '&'


def build_diff_tree(first_tree, second_tree):

    def walk(node1, node2, key=0):
        if not isinstance(node1, dict) or not isinstance(node2, dict):

            return pair_gen(node1, node2, key)

        if isinstance(node1, dict) and isinstance(node2, dict):
            sorted_children = sorted(set(node1) | set(node2))

        diff_children = list(map(
            lambda child: walk(node1.get(child, EMPTY_VALUE), node2.get(child, EMPTY_VALUE), child),
            sorted_children))

        new_children = {}
        for child in diff_children:
            new_children.update(child)

        if key != 0:
            new_children = {key: new_children}

        return new_children

    return walk(first_tree, second_tree)


def pair_gen(node1, node2, key):

    value1 = node1
    value2 = node2
    if value1 == EMPTY_VALUE:
        return {key: {'action': 'add', 'node2': value2}}
    if value2 == EMPTY_VALUE:
        return {key: {'action': 'remove', 'node1': value1}}
    if value1 == value2:
        return {key: {'action': 'nested', 'node1': value1}}
    if value1 != value2 and not isinstance(value1, dict) or not isinstance(value2, dict):
        return {key: {'action': 'changed', 'node1': value1, 'node2': value2}}
