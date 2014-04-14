import lexer
import ply.yacc as yacc
import ply.lex as lex


class Node:
    def __init__(self, value, *children):
        self.value = value
        self.children = children

    def __str__(self):
        return self.traverse(1)

    def traverse(self, i):
        s = self.value
        indent = "\n" + i*' |'
        for child in self.children:
            #print children
            if child is not None: #todo: figure out epsilon
                s += indent + child.traverse(i+1)
        return s


def p_program(p):
    """
    program : statement_list translation_unit
    """
    p[0] = Node('program', p[1], p[2])

def p_block(p):
    """
    block : ':' NEWLINE INDENT statement_list 
    """
    p[0] = Node('block', p[3])

def p_function_definition(p):
    """
    function_definition   : '#' ID block
                          | '#' ID parameter_declaration block
    """
    if len(p) == 4:
        p[0] = Node('function_definition', p[2], p[3])
    else:
        p[0] = Node('function_definition', p[2], p[3], p[4])

def p_translation_unit(p):
    """
    translation_unit    : epsilon
                        | translation_unit
                        | translation_unit function_definition
    """
    if len(p) == 2:
        p[0] = Node('translation_unit', p[1])
    else:
        p[0] = Node('translation_unit', p[1], p[2])

def p_parameter_declaration(p):
    """
    parameter_declaration   : variable_expression
                            | parameter_declaration ',' variable_expression
                            | 
    """
    if len(p) == 2:
        p[0] = Node('parameter_declaration', p[1])
    else:
        p[0] = Node('parameter_declaration', p[1], p[3])

def p_statement_list(p):
    """
    statement_list  : statement
                    | statement_list statement
    """
    if len(p) == 3:
        p[0] = Node('statement_list', p[1], p[2])
    else:
        p[0] = Node('statement_list', p[1])

def p_statement(p):
    """
    statement   : expression_statement
    """
    p[0] = Node('statement', p[1])

def p_return_statement(p):
    """
    return_statement    : 'return' expression_statement
    """
    p[0] = Node('return_statement', p[2])

def p_expression_statement(p):
    """
    expression_statement    : expression NEWLINE
                            | NEWLINE
    """
    if len(p) == 3:
        p[0] = Node('expression_statement', p[1])
    else:
        p[0] = Node('expression_statement')

def p_primary_expression(p):
    """
    primary_expression : function_expression
    """
    p[0] = Node('primary_expression', p[1])

def p_selection_statement(p):
    """
    selection_statement : 'if' expression block
                        | 'if' expression block 'else' block
    """
    if len(p) == 4:
        p[0] = Node('selection_statement', p[2], p[3])
    else:
        p[0] = Node('selection_statement', p[2], p[3], p[5])

def p_iteration_statement(p):
    """
    iteration_statement    : 'for' ID 'in' primary-expression block
                            | 'for' ID 'in' primary-expression ',' primary-expression block
                            | 'while' expression block
    """
    if len(p) == 4:
        p[0] = Node('iteration_statement', p[2], p[3])
    elif len(p) == 6:
        p[0] = Node('iteration_statement', p[2], p[4], p[5])
    else:
        p[0] = Node('iteration_statement', p[2], p[4], p[6], p[7])

def p_function_expression(p):
    """
    function_expression : '#' ID parameters
    """
    hash = Node(p[1])
    iden = Node(p[2])
    p[0] = Node('function_expression', hash, iden, p[3])


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
    variable_expression : '@' ID
    """
    at = Node(p[1])
    iden = Node(p[2])
    p[0] = Node('variable_expression', at, iden)


def p_epsilon(p):
    """
    epsilon :
    """
    pass


def p_error(p):
    if p is None:
        tok = lex.LexToken()
        tok.value = '\n'
        tok.type = 'NEWLINE'
        yacc.errok()
        return tok




tokens = lexer.tokens

if __name__ == '__main__':
    my_lex = lexer.get_lex()
    parser = yacc.yacc()

    ## feed it some input data - test - how do we automate this?
    data = '#grayscale @image1\r\n' #todo can we avoid requiring newline?

    tree = parser.parse(data, lexer=my_lex)
    print("I made a tree! yay!")
    print(tree)
