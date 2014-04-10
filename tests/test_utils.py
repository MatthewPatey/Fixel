import mock
from src.parser import Node


def get_mock_token(type, value):
    mock_token = mock.MagicMock()
    mock_token.type = type
    mock_token.value = value
    return mock_token


def tree_to_string(tree):
    s = '(' + tree.value
    if hasattr(tree, 'children'):
        for child in tree.children:
            s += ' ' + tree_to_string(child)
    s += ')'
    return s


def string_tree_pretty_version(tree_string):
    """
    Don't use in tests! For debuggging only, meant for human to view tree in easier to read format
    """
    no_spaces_tree_string = tree_string.replace(' ', '')
    tree, final_index = string_to_tree(no_spaces_tree_string, 0)

    if final_index < len(no_spaces_tree_string)-1:
        raise ValueError('bad format, matched open parentheses before reaching end of string')
    elif final_index >= len(no_spaces_tree_string):
        raise ValueError('looks like Matt screwed up the string to tree function')

    print(tree)


def string_to_tree(tree_string, index):
    """
    builds node for current level and creates children recursively
    must be given string with no whitespace. For debugging only, don't use in tests
    """

    # child starts with ( character
    if tree_string[index] != '(':
        raise ValueError('invalid tree string format, each subtree must start with \"(\"')
    index += 1

    children = []
    node_name = ''
    i = index
    while i < len(tree_string):
        char = tree_string[i]
        if char == '(':  # new child
            child, new_index = string_to_tree(tree_string, i)
            children.append(child)
            i = new_index
        elif char == ')':  # end of this tree, return
            node = Node(node_name)
            node.children = tuple(children)  # passing tuple to constructor results in nested tuple
            return node, i  # return node and current place in iteration
        else:  # character is part of node name
            node_name += char

        i += 1  # increment to next character

    raise ValueError('bad format, reached end of string with without balancing all open parentheses')


    child_string = tree_string[child_index:]
    while True:
        child, child_string = string_to_tree(child_string)
        children.append(child)

        if child_string[0] == ')':  # end of this subtree
            break
    node.children = tuple(children)
    return node, child_string[1:]
