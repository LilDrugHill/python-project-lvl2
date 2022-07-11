EMPTY_VALUE = '&'


def build_diff(data1, data2):

    def walk(node1, node2, key=None):
        if not isinstance(node1, dict) or not isinstance(node2, dict):
            return generate_node_diff_for_key(node1, node2, key)

        sorted_children = sorted(set(node1) | set(node2))

        diff_children = list(map(
            lambda child: walk(node1.get(child, EMPTY_VALUE), node2.get(child, EMPTY_VALUE), child),
            sorted_children))

        new_children = {}
        for child in diff_children:
            new_children.update(child)

        return {key: new_children} if key else new_children

    return walk(data1, data2)


def generate_node_diff_for_key(node1, node2, key):
    value1 = node1
    value2 = node2
    if value1 == EMPTY_VALUE:
        return {key: {'action': 'add', 'node2': value2}}
    if value2 == EMPTY_VALUE:
        return {key: {'action': 'remove', 'node1': value1}}
    if value1 == value2:
        return {key: {'action': 'nested', 'node1': value1}}

    return {key: {'action': 'changed', 'node1': value1, 'node2': value2}}
