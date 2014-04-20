"""
keys are node names and
values are tables where key is index of child after which to print and value is string to print
"""
strings_table = {
    'function_expression': {
        1: '(', 2: ')'
    },
    'function_definition': {
        1: '(', 2: ')'
    },
    'parameter_declaration': {
        1: ' '
    },
    'return_statement': {
        0: ' '
    },
    'selection_statement': {
        0: ' '
    },
    'iteration_statement': {
        0: ' '
    },
}


"""
keys are node names.
Values are tuples containing index of child after which custom behavior should occur,
string to print if expression evaluates to true,
and lambda taking node argument that executes an expression returning a boolean.
"""
custom_behvavior_table = {
    'iteration_statement': {
        1: (' ', lambda node: len(node.children) > 3),  # print space after ID if in a for loop
        2: (' ', lambda node: len(node.children) > 3),  # print space after 'in' if in a for loop
        4: (' ', lambda node: len(node.children) == 6)  # print space after ',' if in a range for loop
    },
    'logical_NOT_expression': {
        1: (' ', lambda node: len(node.children) == 2)
    },
    'logical_AND_expression': {
        0: (' ', lambda node: len(node.children) == 3),
        1: (' ', lambda node: len(node.children) == 3)
    },
    'logical_OR_expression': {
        0: (' ', lambda node: len(node.children) == 3),
        1: (' ', lambda node: len(node.children) == 3)
    }
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
        if len(node.children) > 0:  # non-leaf
            # obtain custom behavior function, set to None if there isn't one
            # first check if there are child_separator strings e.g. parentheses
            if node.value in strings_table:
                child_separator_strings = strings_table[node.value]
            else:
                child_separator_strings = None

            if node.value in custom_behvavior_table:
                custom_behvaviors = custom_behvavior_table[node.value]
            else:
                custom_behvaviors = None

            # process the children
            for i in range(0, len(node.children)):
                child = node.children[i]
                self.process_tree(child)

                if child_separator_strings is not None and i in child_separator_strings:
                    post_child_string = child_separator_strings[i]
                    self.string_list.append(post_child_string)

                # check if we should call custom function at this iteration
                if custom_behvaviors is not None and i in custom_behvaviors:
                    custom_behvavior_string, custom_behvavior_expression = custom_behvaviors[i]
                    if custom_behvavior_expression(node):
                        self.string_list.append(custom_behvavior_string)
        elif node.value not in ignore:  # leaf
            # if it's a leaf add it to the string list
            self.string_list.append(node.value)
