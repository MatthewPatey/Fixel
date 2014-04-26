from unittest import TestCase
from src import lexer
import test_strings


class LexerTests(TestCase):
	def oneliner_test(self):
		self.run_lexer_on_source(test_strings.oneliner_source, test_strings.oneliner_tokens)

	def indent_test(self):
		self.run_lexer_on_source(test_strings.indent_source, test_strings.indent_tokens)

	def run_lexer_on_source(self, source, expected_tokens):
		my_lex = lexer.get_lex()
		my_lex.input(source)

		for expected_token in expected_tokens:
			actual_token = my_lex.token()
			self.assertEqual(expected_token[0], actual_token.type)
			self.assertEqual(expected_token[1], actual_token.value)

		self.assertIsNone(my_lex.token())  # make sure token stream was exhausted
