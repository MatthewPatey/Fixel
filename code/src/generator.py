import pdb

"""
keys are nodes that should have spaces printed around them, and values say where to print.
1 means before, 2 means after and 3 means both (picture bitwise or).
"""
spaces_table = {
	',': 2,
    'return': 2,
    'if': 2,
    'for': 2,
    'in': 3,
    'while': 2,
    '=': 3,
    'or': 3,
    'and': 3,
    '!=': 3,
    '==': 3,
    '<': 3,
    '>': 3,
    '<=': 3,
    '>=': 3,
    '+': 3,
    '-': 3,
    '*': 3,
    '/': 3,
    'not': 2
}


ignore = ['#', '@', '']

indent_level = 0

class Generator:
    def __init__(self, tree):
        self.string_list = []
        self.tree = tree
        self.process_tree(tree)

    def get_string(self):
        return ''.join(self.string_list)

    def process_tree(self, node):
        #pdb.set_trace()
        if node.value in custom_functions_table:  # call custom processing function
            custom_function = custom_functions_table[node.value]
            custom_function(self, node)
        else:  # if no custom function, use default processing
            # get spaces information
            spaces = spaces_table.get(node.value, 0)
            space_before = spaces & 1
            space_after = spaces & 2

            if space_before:  # add space before processing
                self.string_list.append(' ')

            if len(node.children) > 0:  # non-leaf
                # process the children
                for child in node.children:
                    self.process_tree(child)
            elif node.value not in ignore:  # leaf
                # if it's a leaf add it to the string list
                self.string_list.append(node.value)

            if space_after:
                self.string_list.append(' ')

    def process_function_definition(self, node):
        id_node, parameter_declaration, block = node.children
        self.string_list.append('def ')
        self.process_tree(id_node)
        self.string_list.append('(')
        self.process_tree(parameter_declaration)
        self.string_list.append(')')
        self.process_tree(block)

    def process_function_expression(self, node):
        hashtag, id_node, parameters = node.children
        self.process_tree(id_node)
        self.string_list.append('(')
        self.process_tree(parameters)
        self.string_list.append(')')

    def process_newline(self,node):
        self.string_list.append(node.value)
        for i in range(0, indent_level):
            self.string_list.append('\t')


    def process_indent(self,node):
        global indent_level 
        indent_level += 1
        self.string_list.append('\t')

    def process_dedent(self,node):
        global indent_level 
        indent_level -= 1
        del self.string_list[-1]  #todo worry about index errors

custom_functions_table = {
    'function_definition': Generator.process_function_definition,
    'function_expression': Generator.process_function_expression,
    '\n': Generator.process_newline,
    'INDENT': Generator.process_indent,
    'DEDENT': Generator.process_dedent
}
