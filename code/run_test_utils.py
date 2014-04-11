import argparse
from tests import test_strings, test_utils


if __name__ == '__main__':
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('-t', '--tree-string')
    namespace = arg_parser.parse_args()

    if namespace.tree_string is not None:
        tree_string = getattr(test_strings, namespace.tree_string)
        test_utils.string_tree_pretty_version(tree_string)
