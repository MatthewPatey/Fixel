import argparse
import sys
from src import fixel

if __name__ == '__main__':
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('-v', '--verbose', help='prints every intermediate step in translation',
                            action='store_true', default=False)
    namespace = arg_parser.parse_args()

    result = fixel.translate(verbose=namespace.verbose)
