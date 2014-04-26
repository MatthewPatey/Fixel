'''
source strings
'''

oneliner_source = '#grayscale @image1\n'

indent_source = '''\
if @hey < not 1:
	#sup
#hey @image1
for @image in @images:
	if @image == @image1:
		#hey @image
hey @myImage:
	if @myImage.width > 100:
		if @myImage.height > 50 and @myImage.height < 60:
			@x = 10
		@y = 50
	else:
		@x = 100
		@y = 20
	return @x
'''

function_def_source = '''\
#sup @image1, @image2

sup @myImage1, @myImage2:
	return @myImage1.height + @myImage2.height
'''

or_and_source = '''\
true and false or @str == "cool string"
true and (false or @str == "cool string")
'''

not_source = '''\
@myList = [40, 500]
not 100 <= @myList[1]
'''

'''
token streams
'''

oneliner_tokens = [('#', '#'), ('ID', 'grayscale'), ('@', '@'), ('ID', 'image1'), ('NEWLINE', '\n')]

function_def_tokens = [('#', '#'), ('ID', 'hey'), ('@', '@'), ('ID', 'image1'), (',', ','), ('@', '@'), ('ID', 'image2'), ('NEWLINE', '\n'), ('ID', 'hey'), ('@', '@'), ('ID', 'image1'), (',', ','), ('@', '@'), ('ID', 'image2'), (':', ':'), ('NEWLINE', '\n'), ('INDENT', 'INDENT'), ('RETURN', 'return'), ('@', '@'), ('ID', 'image1'), ('+', '+'), ('@', '@'), ('ID', 'image2'), ('NEWLINE', '\n'), ('DEDENT', 'DEDENT')]

indent_tokens = [('IF', 'if'), ('@', '@'), ('ID', 'hey'), ('<', '<'), ('NOT', 'not'), ('NUMBER', '1'), (':', ':'), ('NEWLINE', '\n'), ('INDENT', 'INDENT'), ('#', '#'), ('ID', 'sup'), ('NEWLINE', '\n'), ('DEDENT', 'DEDENT'), ('#', '#'), ('ID', 'hey'), ('@', '@'), ('ID', 'image1'), ('NEWLINE', '\n'), ('FOR', 'for'), ('@', '@'), ('ID', 'image'), ('IN', 'in'), ('@', '@'), ('ID', 'images'), (':', ':'), ('NEWLINE', '\n'), ('INDENT', 'INDENT'), ('IF', 'if'), ('@', '@'), ('ID', 'image'), ('DUBEQUAL', '=='), ('@', '@'), ('ID', 'image1'), (':', ':'), ('NEWLINE', '\n'), ('INDENT', 'INDENT'), ('#', '#'), ('ID', 'hey'), ('@', '@'), ('ID', 'image'), ('NEWLINE', '\n'), ('DEDENT', 'DEDENT'), ('DEDENT', 'DEDENT'), ('ID', 'hey'), ('@', '@'), ('ID', 'myImage'), (':', ':'), ('NEWLINE', '\n'), ('INDENT', 'INDENT'), ('IF', 'if'), ('@', '@'), ('ID', 'myImage'), ('.', '.'), ('ID', 'width'), ('>', '>'), ('NUMBER', '100'), (':', ':'), ('NEWLINE', '\n'), ('INDENT', 'INDENT'), ('IF', 'if'), ('@', '@'), ('ID', 'myImage'), ('.', '.'), ('ID', 'height'), ('>', '>'), ('NUMBER', '50'), ('AND', 'and'), ('@', '@'), ('ID', 'myImage'), ('.', '.'), ('ID', 'height'), ('<', '<'), ('NUMBER', '60'), (':', ':'), ('NEWLINE', '\n'), ('INDENT', 'INDENT'), ('@', '@'), ('ID', 'x'), ('=', '='), ('NUMBER', '10'), ('NEWLINE', '\n'), ('DEDENT', 'DEDENT'), ('@', '@'), ('ID', 'y'), ('=', '='), ('NUMBER', '50'), ('NEWLINE', '\n'), ('DEDENT', 'DEDENT'), ('ELSE', 'else'), (':', ':'), ('NEWLINE', '\n'), ('INDENT', 'INDENT'), ('@', '@'), ('ID', 'x'), ('=', '='), ('NUMBER', '100'), ('NEWLINE', '\n'), ('@', '@'), ('ID', 'y'), ('=', '='), ('NUMBER', '20'), ('NEWLINE', '\n'), ('DEDENT', 'DEDENT'), ('RETURN', 'return'), ('@', '@'), ('ID', 'x'), ('NEWLINE', '\n'), ('DEDENT', 'DEDENT')]


'''
abstract syntax tress
'''

oneliner_tree = '[program [statement_list [statement [expression_statement [expression [assignment_expression [logical_OR_expression [logical_AND_expression [equality_expression [relational_expression [additive_expression [multiplicative_expression [logical_NOT_expression [intermediate_expression [function_expression [#] [grayscale] [parameters [primary_expression [variable_access_expression [variable_expression [@] [image1]]]]]]]]]]]]]]]] [\n]]]]]'

				

				
'''
python strings
'''

oneliner_python = 'grayscale(image1)\n'