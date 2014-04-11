from unittest import TestCase
import mock
from src import parser
import test_utils
import test_strings


class ParserTests(TestCase):
    def test_test(self):
        self.assertTrue(True)

    def oneliner_test(self):
        self.run_parser_on_tokens(test_strings.oneliner_tokens, test_strings.oneliner_tree)

    def run_parser_on_tokens(self, tokens, expected_tree):
        mock_lex = mock.MagicMock()
        mock_tokens = []
        for token in tokens:
            mock_token = test_utils.get_mock_token(token[0], token[1])
            mock_tokens.append(mock_token)

        # pad iteration in case lookahead goes past end of stream
        mock_lex.token.side_effect = mock_tokens + [None, None]

        my_parser = parser.get_yacc()
        tree = my_parser.parse('', lexer=mock_lex)
        self.assertEqual(expected_tree, test_utils.tree_to_string(tree))
