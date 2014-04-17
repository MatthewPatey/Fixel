import argparse
from tests import test_strings, test_utils


if __name__ == '__main__':
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('-p', '--pretty-string', help='finds the attribute of the test_strings module with the '
                            'given name and prints a pretty version of it if it is a tree string')
    arg_parser.add_argument('-t', '--tree-string', help='prints a tree string built from the given source code')
    namespace = arg_parser.parse_args()

    if namespace.pretty_string is not None:
        tree_string = getattr(test_strings, namespace.pretty_string)
        test_utils.string_tree_pretty_version(tree_string)

    if namespace.tree_string is not None:
        source = namespace.tree_string
        test_utils.tree_string_from_source(source)
