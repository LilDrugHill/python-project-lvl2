def generate_diff(file1, file2):

    def walk(node1, node2, key=0):

        if not isinstance(node1, dict) or not isinstance(node2, dict):
            return pair_gen(node1, node2, key)

        if isinstance(node1, dict) and isinstance(node2, dict):
            sorted_children = sorted(set(node1) | set(node2))

        new_children = list(map(
            lambda child: walk(node1.get(child, '&'), node2.get(child, '&'), child),
            sorted_children))

        return new_tree_gen(key, new_children)

    return walk(file1, file2)


def pair_gen(node1, node2, key):

    value1 = node1
    value2 = node2
    if value1 == '&':
        return (f'+ {key}', value2)
    if value2 == '&':
        return (f'- {key}', value1)
    if value1 == value2:
        return (f'  {key}', value1)
    if value1 != value2 and not isinstance(value1, dict) or not isinstance(value2, dict):
        return (
            (f'- {key}', value1),
            (f'+ {key}', value2),
        )


def new_tree_gen(key, new_children):
    new_sorted_children = []
    new_values = []
    for child in new_children:
        if isinstance(child, dict):
            new_children[new_children.index(child)] = (key, child)
        elif isinstance(child[0], tuple):
            new_sorted_children.append(child[0][0])
            new_sorted_children.append(child[1][0])
            new_values.append(child[0][1])
            new_values.append(child[1][1])
        elif isinstance(child, tuple):
            new_sorted_children.append(child[0])
            new_values.append(child[1])

    new_tree = {key: new_children for key, new_children in zip(new_sorted_children, new_values)}
    if key != 0:
        new_tree = (key, new_tree)
    return new_tree
