import mock
from src import lexer
from src import parser


def get_mock_token(type, value):
    mock_token = mock.MagicMock()
    mock_token.type = type
    mock_token.value = value
    return mock_token


def tree_to_string(tree):
    s = '[' + tree.value
    if hasattr(tree, 'children'):
        for child in tree.children:
            s += ' ' + tree_to_string(child)
    s += ']'
    return s


def tree_string_from_source(source_string):
    """
    runs lexer/parser on source string and outputs tree string from the resulting AST.
    """
    my_lex = lexer.get_lex()
    my_yacc = parser.get_yacc()

    tree = my_yacc.parse(source_string, lexer=my_lex)
    tree_string = tree_to_string(tree)

    print('pretty format:')
    print(tree)
    print('\ntree string:')
    print(repr(tree_string))


def string_tree_pretty_version(tree_string):
    """
    For debuggging, meant for human to view tree in easier to read format
    """
    print('input tree string:\n')
    print(repr(tree_string) + '\n')
    no_spaces_tree_string = tree_string.replace(' ', '')
    tree, final_index = string_to_tree(no_spaces_tree_string, 0)

    if final_index < len(no_spaces_tree_string)-1:
        raise ValueError('bad format, matched open parentheses before reaching end of string')
    elif final_index >= len(no_spaces_tree_string):
        raise ValueError('looks like Matt screwed up the string to tree function')

    print('pretty format:\n')
    print(tree)


def string_to_tree(tree_string, index):
    """
    builds node for current level and creates children recursively
    must be given string with no whitespace.
    """

    # child starts with ( character
    if tree_string[index] != '[':
        raise ValueError('invalid tree string format, each subtree must start with \"(\"')
    index += 1

    children = []
    node_name = ''
    i = index
    while i < len(tree_string):
        char = tree_string[i]
        if char == '[':  # new child
            child, new_index = string_to_tree(tree_string, i)
            children.append(child)
            i = new_index
        elif char == ']':  # end of this tree, return
            node = parser.Node(node_name)
            node.children = tuple(children)  # passing tuple to constructor results in nested tuple
            return node, i  # return node and current place in iteration
        else:  # character is part of node name
            node_name += char

        i += 1  # increment to next character

    raise ValueError('bad format, reached end of string with without balancing all open parentheses')
