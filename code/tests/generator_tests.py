from unittest import TestCase
from src import generator
import test_strings
import test_utils


class GeneratorTests(TestCase):
    def oneliner_test(self):
        self.run_generator_on_tree(test_strings.oneliner_tree, test_strings.oneliner_python)

    def selection_if_test(self):
        self.run_generator_on_tree(test_strings.selection_if_tree, test_strings.selection_if_python)

    def selection_ifelse_test(self):
        self.run_generator_on_tree(test_strings.selection_ifelse_tree, test_strings.selection_ifelse_python)

    def equality_notequal_test(self):
        self.run_generator_on_tree(test_strings.equality_notequal_tree, test_strings.equality_notequal_python)

    def iteration_for_test(self):
        self.run_generator_on_tree(test_strings.iteration_for_tree, test_strings.iteration_for_python)

    def multiplicative_test(self):
        self.run_generator_on_tree(test_strings.multiplicative_tree, test_strings.multiplicative_python)

    def run_generator_on_tree(self, tree_string, expected_python):
        tree_string_no_ws = tree_string.replace(' ', '')
        tree, _ = test_utils.string_to_tree(tree_string_no_ws, 0)
        gen = generator.Generator(tree)
        actual_python = gen.get_string()
        self.assertEqual(expected_python, actual_python)
