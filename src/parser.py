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

def p_translation_unit(p):
    '''
    translation_unit    : translation_unit function_definition 
                        | epsilon    
    '''
    if len(p) == 2:
        p[0] = Node('translation_unit', p[1], p[2])
    else:
        p[0] = []

def p_function_definition(p):
    """
    p_function_definition   :‘#’ ID block
                            |‘#’ ID parameter_declaration block
    """
    at = Leaf(p[1])
    ident = Leaf(p[2])
    p[0] = Node(at, ident)

def p_parameter_decalration(p):
    """
    parameter_decalration    
    """

def p_statement_list(p):
    """
    statement_list  : statement
                    | statement statement_list 
    """
    if len(p) == 2:
        p[0] = Node('statement_list', p[1], p[2])
    else:
        p[0] = Node('statement_list', p[1])

def p_statement(p):
    """
    statement   : expression_statement
                | selection_statement
                | iteration_statement
                | return_statement
    """
    p[0] = Node('statement', p[1])



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
