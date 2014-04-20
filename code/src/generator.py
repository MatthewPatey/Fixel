

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

            # obtain custom behavior function, set to None if there isn't one
            if node.value in custom_function_table.keys():
                custom_index, custom_function = custom_function_table[node.value]
            else:
                custom_function = None

            # add pre processing info
            if current_tuple[0] is not None:
                self.string_list.append(current_tuple[0])

            # process the children
            for i in range(0, len(node.children)):
                child = node.children[i]
                self.process_tree(child)

                # check if we should call custom function at this iteration
                if custom_function is not None and custom_index == i:
                    custom_function(self, node)

            # add post processing info
            if current_tuple[1] is not None:
                self.string_list.append(current_tuple[1])
        elif node.value not in ignore:
            # if it's a leaf add it to the string list
            self.string_list.append(node.value)

    def function_expression_custom_function(self, node):
        """
        handles case of no parameters in a function expression
        """
        if len(node.children[2].value) == 0:
            self.string_list.append('()')

    def function_definition_custom_function(self, node):
        """
        handles case of no parameters in a function definition
        """
        if len(node.children) == 3:
            self.string_list.append('()')


"""
keys are node names (grammar sybmols) and
values are tuple of strings to print before and after the children are processes
"""
pre_post_table = {
    'parameters': ('(', ')'),
    'parameter_declaration': ('(', ')')
}


"""
keys are node names and values are tuples containing index of child after which to call
function and a function that allow custom behavior for a given node type
function is an instance method of Generator class and takes a node argument
"""
custom_function_table = {
    'function_expression': (1, Generator.function_expression_custom_function),
    'function_definition': (1, Generator.function_definition_custom_function)
}


ignore = ['#', '@', '']
