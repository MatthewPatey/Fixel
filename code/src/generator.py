

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
            # first check if there are preprocess strings (paren, cnewline, etc)
            if node.value in pre_post_table.keys():
                current_tuple = pre_post_table[node.value]
            else:
                current_tuple = (None, None)
            # add pre processing info
            if current_tuple[0] is not None:
                self.string_list.append(current_tuple[0])

            # process the children
            for child in node.children:
                self.process_tree(child)

            # add post processing info
            if current_tuple[1] is not None:
                self.string_list.append(current_tuple[1])

            # execute custom behavior before returning
            if node.value in custom_function_table.keys():
                custom_function = custom_function_table[node.value]
                custom_function(self, node)
        elif node.value not in ignore:
            # if it's a leaf add it to the string list
            self.string_list.append(node.value)

    def function_expression_custom_function(self, node):
        """
        handles case of no parameters in a function expression
        """
        if len(node.children[2].value) == 0:
            self.string_list.append('()')


"""
keys are node names (grammar sybmols) and
values are tuple of strings to print before and after the children are processes
"""
pre_post_table = {
    'parameters': ('(', ')'),
    'expression_statement': (None, '\n')
}


# keys are node names and values are functions that allow custom behavior for a given node type
custom_function_table = {
    'function_expression': Generator.function_expression_custom_function
}


ignore = ['#', '@', '']
