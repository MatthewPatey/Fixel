'''
source strings
'''

oneliner_source = '#grayscale @image1'


'''
token streams
'''

oneliner_tokens = [('#', '#'), ('ID', 'grayscale'), ('@', '@'), ('ID', 'image1')]


'''
abstract syntax tress
'''

oneliner_tree = '(program (statement_list (statement (expression_statement (primary_expression ' \
                '(function_expression (#) (grayscale) (parameters (variable_access_expression ' \
                '(variable_expression (@) (image1))))))))) ())'
