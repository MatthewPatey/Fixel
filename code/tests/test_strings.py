'''
source strings
'''

oneliner_source = '#grayscale @image1\n'

indent_source = 'if @hey < not 1:\n\t#sup\n#hey @image1,@image2\n'


'''
token streams
'''

oneliner_tokens = [('#', '#'), ('ID', 'grayscale'), ('@', '@'), ('ID', 'image1'), ('NEWLINE', '\n')]


'''
abstract syntax tress
'''

oneliner_tree = '[program [statement_list [statement [expression_statement [expression [assignment_expression [logical_OR_expression [logical_AND_expression [equality_expression [relational_expression [additive_expression [multiplicative_expression [logical_NOT_expression [intermediate_expression [function_expression [#] [grayscale] [parameters [primary_expression [variable_access_expression [variable_expression [@] [image1]]]]]]]]]]]]]]]] [\n]]]]]'

				

				
'''
python strings
'''

oneliner_python = 'grayscale(image1)\n'