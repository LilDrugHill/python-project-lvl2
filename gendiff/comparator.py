EMPTY_VALUE = '&'


def build_diff_tree(first_tree, second_tree):

    def walk(node1, node2, key=0):
        if not isinstance(node1, dict) or not isinstance(node2, dict):

            return pair_gen(node1, node2, key)

        if isinstance(node1, dict) and isinstance(node2, dict):
            sorted_children = sorted(set(node1) | set(node2))

        new_children = list(map(
            lambda child: walk(node1.get(child, EMPTY_VALUE), node2.get(child, EMPTY_VALUE), child),
            sorted_children))

        new_sorted_children, new_values = new_children_and_values_gen(new_children)

        new_tree = {key: new_children for key, new_children in zip(new_sorted_children, new_values)}

        if key != 0:
            new_tree = {key: new_tree}

        return new_tree

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


def new_children_and_values_gen(new_children):
    new_sorted_children = []
    new_values = []
    for child in new_children:
        child_key = list(child.keys())[0]
        action = child[child_key].get('action')
        if action == 'changed':
            new_sorted_children.append(f'-{child_key}')
            new_sorted_children.append(f'+{child_key}')
            new_values.append(child[child_key]['node1'])
            new_values.append(child[child_key]['node2'])
        elif action == 'add':
            new_sorted_children.append(f'+{child_key}')
            new_values.append(child[child_key]['node2'])
        elif action == 'remove':
            new_sorted_children.append(f'-{child_key}')
            new_values.append(child[child_key]['node1'])
        elif action == 'nested':
            new_sorted_children.append(f'{child_key}')
            new_values.append(child[child_key]['node1'])
        else:
            new_sorted_children.append(f'{child_key}')
            new_values.append(child[child_key])

    return new_sorted_children, new_values
