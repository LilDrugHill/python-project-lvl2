EMPTY_VALUE = '&'


def build_diff(first_tree, second_tree):

    def walk(node1, node2, key=None):
        if not isinstance(node1, dict) or not isinstance(node2, dict):
            return choose_action(node1, node2, key)

        sorted_children = sorted(set(node1) | set(node2))

        diff_children = list(map(
            lambda child: walk(node1.get(child, EMPTY_VALUE), node2.get(child, EMPTY_VALUE), child),
            sorted_children))

        new_children = {}
        for child in diff_children:
            new_children.update(child)

        return {key: new_children} if key else new_children

    return walk(first_tree, second_tree)


def choose_action(node1, node2, key):
    value1 = node1
    value2 = node2
    if value1 == EMPTY_VALUE:
        return {key: {'action': 'add', 'node2': value2}}
    if value2 == EMPTY_VALUE:
        return {key: {'action': 'remove', 'node1': value1}}
    if value1 == value2:
        return {key: {'action': 'nested', 'node1': value1}}

    return {key: {'action': 'changed', 'node1': value1, 'node2': value2}}
