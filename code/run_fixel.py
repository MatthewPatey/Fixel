import argparse
from src import fixel

arg_parser = argparse.ArgumentParser()
arg_parser.add_argument('-v', '--verbose', help='prints every intermediate step in translation',
						action='store_true', default=False)
arg_parser.add_argument('-f', '--fixel-file', type=argparse.FileType('r'))
namespace = arg_parser.parse_args()
if namespace.fixel_file:
	source_string = namespace.fixel_file.read()
	file_name = namespace.fixel_file.name
	namespace.fixel_file.close()
	result = fixel.translate(source_string, namespace.verbose)
	f = open(file_name.split('.')[0] + '.py', 'w')
	f.write(result)
	f.close()
else:
	result = fixel.translate(verbose=namespace.verbose)
