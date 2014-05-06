import argparse
from src import fixel

arg_parser = argparse.ArgumentParser()
arg_parser.add_argument('-v', '--verbose', help='prints every intermediate step in translation',
						action='store_true', default=False)
arg_parser.add_argument('-f', '--fixel-file', type=argparse.FileType('r'))
namespace = arg_parser.parse_args()
if namespace.fixel_file:
	source_string = namespace.fixel_file.read()
	result = fixel.translate(source_string, namespace.verbose)
else:
	result = fixel.translate(verbose=namespace.verbose)
