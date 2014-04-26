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
        s = repr(self.value)
        indent = "\n" + i*' |'
        for child in self.children:
            #print children
            if len(child.value) > 0:
                s += indent + child.traverse(i+1)
        return s


def p_program(p):
    """
    program : statement_list
            | statement_list translation_unit

    """
    if len(p) == 2:
        p[0] = Node('program', p[1])
    else:
        p[0] = Node('program', p[1], p[2])

def p_block(p):
    """
    block : ':' NEWLINE INDENT statement_list DEDENT
    """
    p[0] = Node('block', Node(p[1]), Node(p[2]), Node(p[3]), p[4], Node(p[5]))


def p_function_definition(p):
    """
    function_definition   : ID parameter_declaration block
    """
    id_node = Node(p[1])
    p[0] = Node('function_definition', id_node, p[2], p[3])

def p_translation_unit(p):
    """
    translation_unit    : function_definition
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
    """
    if len(p) == 2:
        p[0] = Node('parameter_declaration', p[1])
    else:
        p[0] = Node('parameter_declaration', p[1], Node(p[2]), p[3])

def p_parameter_declaration_eps(p):
    """
    parameter_declaration   : epsilon
    """
    p[0] = p[1]

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
                | selection_statement
                | iteration_statement
                | return_statement
    """
    p[0] = Node('statement', p[1])

def p_return_statement(p):
    """
    return_statement    : RETURN expression_statement
    """
    p[0] = Node('return_statement', Node(p[1]), p[2])

def p_expression_statement(p):
    """
    expression_statement    : expression NEWLINE
                            | NEWLINE
    """
    if len(p) == 3:
        p[0] = Node('expression_statement', p[1], Node(p[2]))
    else:
        p[0] = Node('expression_statement', Node(p[1]))

def p_selection_statement(p):
    """
    selection_statement : IF expression block
                        | IF expression block ELSE block
    """
    if_node = Node(p[1])
    if len(p) == 4:
        p[0] = Node('selection_statement', if_node, p[2], p[3])
    else:
        p[0] = Node('selection_statement', if_node, p[2], p[3], Node(p[4]), p[5])

def p_iteration_statement(p):
    """
    iteration_statement     : FOR variable_expression IN primary_expression block
                            | FOR variable_expression IN primary_expression ',' primary_expression block
                            | WHILE expression block
    """
    if len(p) == 4:
        p[0] = Node('iteration_statement', Node(p[1]), p[2], p[3])
    else:
        for_node = Node(p[1])
        #id_node = Node(p[2])
        in_node = Node(p[3])
        if len(p) == 6:
            p[0] = Node('iteration_statement', for_node, p[2], in_node, p[4], p[5])
        else:
            p[0] = Node('iteration_statement', for_node, p[2], in_node, p[4], Node(p[5]), p[6], p[7])

def p_expression(p):
    """
    expression  : assignment_expression
    """
    p[0] = Node('expression', p[1])

def p_assignment_expression(p):
    """
    assignment_expression   : variable_expression '=' assignment_expression
                            | logical_OR_expression
    """
    if len(p) == 2:
        p[0] = Node('assignment_expression', p[1])
    else:
        p[0] = Node('assignment_expression', p[1], Node(p[2]), p[3])
        
def p_logical_OR_expression(p):
    """
    logical_OR_expression   : logical_AND_expression
                            | logical_OR_expression OR logical_AND_expression
    """
    if len(p) == 2:
        p[0] = Node('logical_OR_expression', p[1])
    else:
        p[0] = Node('logical_OR_expression', p[1], Node(p[2]), p[3])

def p_logical_AND_expression(p):
    """
    logical_AND_expression   : equality_expression
                            | logical_AND_expression AND equality_expression
    """
    if len(p) == 2:
        p[0] = Node('logical_AND_expression', p[1])
    else:
        p[0] = Node('logical_AND_expression', p[1], Node(p[2]), p[3])

def p_equality_expression(p):
    """
    equality_expression   : relational_expression
                          | equality_expression DUBEQUAL relational_expression
                          | equality_expression NEQUAL relational_expression
    """
    if len(p) == 2:
        p[0] = Node('equality_expression', p[1])
    else:
        p[0] = Node('equality_expression', p[1], Node(p[2]), p[3])

def p_relational_expression(p):
    """
    relational_expression   : additive_expression
                            | relational_expression '<' additive_expression
                            | relational_expression '>' additive_expression
                            | relational_expression LESSTHANEQ additive_expression
                            | relational_expression GREATERTHANEQ additive_expression
    """
    if len(p) == 2:
        p[0] = Node('relational_expression', p[1])
    else:
        p[0] = Node('relational_expression', p[1], Node(p[2]), p[3])

def p_additive_expression(p):
    """
    additive_expression : multiplicative_expression 
                        | additive_expression '+' multiplicative_expression 
                        | additive_expression '-' multiplicative_expression
    """
    if len(p) == 2:
        p[0] = Node('additive_expression', p[1])
    else:
        p[0] = Node('additive_expression', p[1], Node(p[2]), p[3])

def p_multiplicative_expression(p):
    """
    multiplicative_expression   : logical_NOT_expression
                                | multiplicative_expression '*' logical_NOT_expression
                                | multiplicative_expression '/' logical_NOT_expression
    """
    if len(p) == 2:
        p[0] = Node('multiplicative_expression', p[1])
    else:
        p[0] = Node('multiplicative_expression', p[1], Node(p[2]), p[3])

def p_logical_NOT_expression(p):
    """
    logical_NOT_expression  : intermediate_expression
                            | NOT logical_NOT_expression
    """
    if len(p) == 2:
        p[0] = Node('logical_NOT_expression', p[1])
    else:
        p[0] = Node('logical_NOT_expression', Node(p[1]), p[2])

def p_intermediate_expression(p):
    """
    intermediate_expression     : primary_expression
                                | function_expression
    """
    p[0] = Node('intermediate_expression', p[1])

def p_primary_expression_token(p):
    """
    primary_expression  : STRING
                        | NUMBER
                        | TRUE
                        | FALSE
    """
    p[0] = Node(p[1])

def p_primary_expression(p):
    """
    primary_expression  : variable_access_expression
                        | '[' parameters ']'
                        | '(' expression ')'
    """
    if len(p) == 2:
        p[0] = Node('primary_expression', p[1])
    else: 
        p[0] = Node('primary_expression', Node(p[1]), p[2], Node(p[3]))

def p_function_expression(p):
    """
    function_expression : '#' ID parameters
    """
    hashtag = Node(p[1])
    iden = Node(p[2])
    p[0] = Node('function_expression', hashtag, iden, p[3])

def p_parameters(p):
    """
    parameters : primary_expression
               | parameters ',' primary_expression
    """
    if len(p) == 2:
        p[0] = Node('parameters', p[1])
    else:
        p[0] = Node('parameters', p[1], Node(p[2]), p[3])

def p_parameters_eps(p):
    """
    parameters  : epsilon
    """
    p[0] = p[1]

def p_variable_access_expression(p):
    """
    variable_access_expression : variable_expression
                               | variable_access_expression '.' ID
                               | variable_access_expression '[' primary_expression ']'
    """
    if len(p) == 2:
        p[0] = Node('variable_access_expression', p[1])
    elif len(p) == 4:
        p[0] = Node('variable_access_expression', p[1], Node(p[2]), Node(p[3]))
    else:
        p[0] = Node('variable_access_expression', p[1], Node(p[2]), p[3], Node(p[4]))

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
    p[0] = Node('')

"""
def p_error(p):
    if p is None:
        tok = lex.LexToken()
        tok.value = '\n'
        tok.type = 'NEWLINE'
        yacc.errok()
        return tok
"""

tokens = lexer.tokens


def get_yacc():
    return yacc.yacc()
