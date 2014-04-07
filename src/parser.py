class Node:
    def __init__(self, type, *children):
        self.type = type
        self.children = children


class Leaf:
    def __init__(self, token):
        self.token = token[0]
        if len(tuple) == 2:
            self.value = token[1]


def p_program(p):
    """
    program : statement_list translation_unit
    """
    p[0] = Node('program', p[1], p[2])


def p_expression_statement(p):
    """
    expression_statement : expression NEWLINE
    """
    p[0] = Node('expression_statement', p[1])


def p_primary_expression(p):
    """
    primary_expression : function_expression
    """
    p[0] = Node('primary_expression', p[1])


def p_function_expression(p):
    """
    function_expression : ‘#’ ID parameters
    """
    hashtag = Leaf(p[1])
    iden = Leaf(p[2])
    p[0] = Node('function_expression', hashtag, iden, p[3])


def p_parameters(p):
    """
    parameters : variable_access_expression
    """
    p[0] = Node('parameters', p[1])


def p_variable_access_expression(p):
    """
    variable_access_expression : variable_expression
    """
    p[0] = Node('variable_access_expression', p[1])


def p_variable_expression(p):
    """
    variable_expression : ‘@’ ID
    """
    at = Leaf(p[1])
    iden = Leaf(p[2])
    p[0] = Node('variable_expression', at, iden)


def p_epsilon(p):
    """
    epsilon :
    """
    pass
