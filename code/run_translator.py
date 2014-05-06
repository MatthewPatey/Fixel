import argparse
import os
from src import translator

arg_parser = argparse.ArgumentParser()
arg_parser.add_argument('-v', '--verbose', help='prints every intermediate step in translation',
						action='store_true', default=False)
arg_parser.add_argument('-f', '--fixel-file', type=argparse.FileType('r'))
namespace = arg_parser.parse_args()

if namespace.fixel_file:
	source_string = namespace.fixel_file.read()
	file_name = namespace.fixel_file.name
	namespace.fixel_file.close()

	pwd = os.getcwd()
	script_dir = os.path.dirname(__file__)  # directory this script is in
	os.chdir(script_dir)  # change directory so parse outputs are in right place

	result = translator.translate(source_string, namespace.verbose)

	os.chdir(pwd)  # go back to original pwd before writing out file
	f = open(file_name.split('.')[0] + '.py', 'w')
	f.write(result)
	f.close()
else:
	result = translator.translate(verbose=namespace.verbose)
