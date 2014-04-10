from unittest import TestCase
import mock
from src import parser
import test_utils


expected_tree = '(program (statement_list (statement (expression_statement (primary_expression ' \
                '(function_expression (#) (grayscale) (parameters (variable_access_expression ' \
                '(variable_expression (@) (image1))))))))) ())'


class ParserTest(TestCase):
    def test_test(self):
        self.assertTrue(True)

    def simple_test(self):
        mock_lex = mock.MagicMock()
        tokens = [('#', '#'), ('ID', 'grayscale'), ('@', '@'), ('ID', 'image1')]
        mock_tokens = []
        for token in tokens:
            mock_token = test_utils.get_mock_token(token[0], token[1])
            mock_tokens.append(mock_token)
        mock_lex.token.side_effect = mock_tokens + [None, None]

        my_parser = parser.get_yacc()
        tree = my_parser.parse('', lexer=mock_lex)
        self.assertEqual(expected_tree, test_utils.tree_to_string(tree))
