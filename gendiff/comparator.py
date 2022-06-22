EMPTY_VALUE = '&'


def comparator(first_tree, second_tree):

    def walk(node1, node2, key=0):

        if not isinstance(node1, dict) or not isinstance(node2, dict):
            return pair_gen(node1, node2, key)

        if isinstance(node1, dict) and isinstance(node2, dict):
            sorted_children = sorted(set(node1) | set(node2))

        new_children = list(map(
            lambda child: walk(node1.get(child, EMPTY_VALUE), node2.get(child, EMPTY_VALUE), child),
            sorted_children))

        return new_tree_gen(key, new_children)

    return walk(first_tree, second_tree)


def pair_gen(node1, node2, key):

    value1 = node1
    value2 = node2
    if value1 == EMPTY_VALUE:
        return (f'+{key}', value2)
    if value2 == EMPTY_VALUE:
        return (f'-{key}', value1)
    if value1 == value2:
        return (f'%{key}', value1)  # symbol % meens equality
    if value1 != value2 and not isinstance(value1, dict) or not isinstance(value2, dict):
        return (
            (f'-{key}', value1),
            (f'+{key}', value2),
        )


def new_tree_gen(key, new_children):
    new_sorted_children = []
    new_values = []
    for child in new_children:  # new_children=[(+/-/%key, value), ((-key, value1), (+key, value2))]
        diff_key = child[0]
        diff_value = child[1]
        if isinstance(diff_key, tuple):  # input ((-key, value1), (+key, value2))
            neg_key = child[0][0]
            pos_key = child[1][0]
            neg_key_value = child[0][1]
            pos_key_value = child[1][1]
            new_sorted_children.append(neg_key)
            new_sorted_children.append(pos_key)
            new_values.append(neg_key_value)
            new_values.append(pos_key_value)
        else:  # input (+/-/%key, value)
            new_sorted_children.append(diff_key)
            new_values.append(diff_value)

    new_tree = {key: new_children for key, new_children in zip(new_sorted_children, new_values)}
    if key != 0:
        new_tree = (key, new_tree)
    return new_tree
