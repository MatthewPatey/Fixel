from parser import Node, Leaf


lookup_table = {
    'parameters': ('(', ')'),
    'expression_statement': (None, '\n')
}


class Generator:
    def __init__(self, tree):
        self.string_list = []
        self.tree = tree
        self.process_tree(tree)

    def get_string(self):
        return ''.join(self.string_list)

    def process_tree(self, node):
        if isinstance(node, Node):
            if node.type in lookup_table.keys():
                current_tuple = lookup_table[node.type]
            else:
                current_tuple = (None, None)

            if current_tuple[0] is not None:
                self.string_list.append(current_tuple[0])

            for child in node.children:
                self.process_tree(child)

            if current_tuple[1] is not None:
                self.string_list.append(current_tuple[1])
        elif isinstance(node, Leaf):
            self.string_list.append(node.value)
        else:
            print 'error!'  # todo errors uh oh
