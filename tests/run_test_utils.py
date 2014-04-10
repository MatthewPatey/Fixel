import argparse
import test_utils
import parser_tests
from tests import test_strings


if __name__ == '__main__':
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('-s', '--string-name')
    namespace = arg_parser.parse_args()

    if 'string_name' in vars(namespace).keys():
        tree_string = getattr(test_strings, namespace.string_name)
        test_utils.string_tree_pretty_version(tree_string)
