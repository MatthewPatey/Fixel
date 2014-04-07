class Node:
    def __init__(self, type, *children):
        self.type = type
        self.children = children

class Leaf:
    def __init__(self, token, value):
        self.token = token
        self.value = value

def p_program(p):
    '''
    program : statement-list translation-unit
    '''
    p[0] = Node('program', p[1], p[2])

def p_epsilon(p):
    '''
    epsilon :
    '''
    pass
