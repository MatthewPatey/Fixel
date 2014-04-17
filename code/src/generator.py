lookup_table = {
    'parameters': ('(', ')'),
    'expression_statement': (None, '\n')
}


ignore = ['#', '@', '']


class Generator:
    def __init__(self, tree):
        self.string_list = []
        self.tree = tree
        self.process_tree(tree)

    def get_string(self):
        return ''.join(self.string_list)

    def process_tree(self, node):
        if len(node.children) > 0:
            # if it's not a leaf, process it
            # first check if there are preprocess strings (paren, newline, etc)
            if node.value in lookup_table.keys():
                current_tuple = lookup_table[node.value]
            else:
                current_tuple = (None, None)
            # add pre/post processing info
            if current_tuple[0] is not None:
                self.string_list.append(current_tuple[0])

            # process the children
            for child in node.children:
                self.process_tree(child)
            # add info for the current node to the list
            if current_tuple[1] is not None:
                self.string_list.append(current_tuple[1])
        elif node.value not in ignore:
            # if it's a leaf add it to the string list
            self.string_list.append(node.value)
