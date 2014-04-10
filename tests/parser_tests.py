from unittest import TestCase
import mock
from src import parser


class ParserTest(TestCase):
    def test_test(self):
        self.assertTrue(True)

    def simple_test(self):
        expected_tree = '(program (statement_list (statement (expression_statement (primary_expression ' \
                        '(function_expression (#) (grayscale) (parameters (variable_access_expression ' \
                        '(variable_expression (@) (image1))))))))) ())'

        mock_lex = mock.MagicMock()
        tokens = [('#', '#'), ('ID', 'grayscale'), ('@', '@'), ('ID', 'image1')]
        mock_tokens = []
        for token in tokens:
            mock_token = get_mock_token(token[0], token[1])
            mock_tokens.append(mock_token)
        mock_lex.token.side_effect = mock_tokens + [None, None]

        my_parser = parser.get_yacc()
        tree = my_parser.parse('', lexer=mock_lex)
        self.assertEqual(expected_tree, tree_to_string(tree))


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
