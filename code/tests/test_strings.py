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

selection_if_source='''\
if @x<1:
	@y=5
'''

selection_ifelse_source='''\
if @x>1 and @y>=1:
	@y=@y-5
else:
	@y=3
'''

iteration_for_source='''\
for @image in @images:
	@x=@x+1
'''

multiplicative_source='''\
@x=@y*5
@y=@x/5
'''

equality_notequal_source='''\
@test=(5!=3)
'''

color_setting_source='''\
@red = color(0,0,0)
@image1[302,19] = @red
'''


'''
token streams
'''


oneliner_tokens = [('#', '#'), ('ID', 'grayscale'), ('@', '@'), ('ID', 'image1'), ('NEWLINE', '\n')]

indent_tokens = [('IF', 'if'), ('@', '@'), ('ID', 'hey'), ('<', '<'), ('NOT', 'not'), ('NUMBER', '1'), (':', ':'), ('NEWLINE', '\n'), ('INDENT', 'INDENT'), ('#', '#'), ('ID', 'sup'), ('NEWLINE', '\n'), ('DEDENT', 'DEDENT'), ('#', '#'), ('ID', 'hey'), ('@', '@'), ('ID', 'image1'), ('NEWLINE', '\n'), ('FOR', 'for'), ('@', '@'), ('ID', 'image'), ('IN', 'in'), ('@', '@'), ('ID', 'images'), (':', ':'), ('NEWLINE', '\n'), ('INDENT', 'INDENT'), ('IF', 'if'), ('@', '@'), ('ID', 'image'), ('DUBEQUAL', '=='), ('@', '@'), ('ID', 'image1'), (':', ':'), ('NEWLINE', '\n'), ('INDENT', 'INDENT'), ('#', '#'), ('ID', 'hey'), ('@', '@'), ('ID', 'image'), ('NEWLINE', '\n'), ('DEDENT', 'DEDENT'), ('DEDENT', 'DEDENT'), ('ID', 'hey'), ('@', '@'), ('ID', 'myImage'), (':', ':'), ('NEWLINE', '\n'), ('INDENT', 'INDENT'), ('IF', 'if'), ('@', '@'), ('ID', 'myImage'), ('.', '.'), ('ID', 'width'), ('>', '>'), ('NUMBER', '100'), (':', ':'), ('NEWLINE', '\n'), ('INDENT', 'INDENT'), ('IF', 'if'), ('@', '@'), ('ID', 'myImage'), ('.', '.'), ('ID', 'height'), ('>', '>'), ('NUMBER', '50'), ('AND', 'and'), ('@', '@'), ('ID', 'myImage'), ('.', '.'), ('ID', 'height'), ('<', '<'), ('NUMBER', '60'), (':', ':'), ('NEWLINE', '\n'), ('INDENT', 'INDENT'), ('@', '@'), ('ID', 'x'), ('=', '='), ('NUMBER', '10'), ('NEWLINE', '\n'), ('@', '@'), ('ID', 'y'), ('=', '='), ('NUMBER', '50'), ('NEWLINE', '\n'), ('DEDENT', 'DEDENT'), ('DEDENT', 'DEDENT'), ('ELSE', 'else'), (':', ':'), ('NEWLINE', '\n'), ('INDENT', 'INDENT'), ('@', '@'), ('ID', 'x'), ('=', '='), ('NUMBER', '100'), ('NEWLINE', '\n'), ('@', '@'), ('ID', 'y'), ('=', '='), ('NUMBER', '20'), ('NEWLINE', '\n'), ('DEDENT', 'DEDENT'), ('RETURN', 'return'), ('@', '@'), ('ID', 'x'), ('NEWLINE', '\n'), ('DEDENT', 'DEDENT')]

function_def_tokens = [('#', '#'), ('ID', 'sup'), ('@', '@'), ('ID', 'image1'), (',', ','), ('@', '@'), ('ID', 'image2'), ('NEWLINE', '\n'), ('ID', 'sup'), ('@', '@'), ('ID', 'myImage1'), (',', ','), ('@', '@'), ('ID', 'myImage2'), (':', ':'), ('NEWLINE', '\n'), ('INDENT', 'INDENT'), ('RETURN', 'return'), ('@', '@'), ('ID', 'myImage1'), ('.', '.'), ('ID', 'height'), ('+', '+'), ('@', '@'), ('ID', 'myImage2'), ('.', '.'), ('ID', 'height'), ('NEWLINE', '\n'), ('DEDENT', 'DEDENT')]

or_and_tokens = [('TRUE', 'true'), ('AND', 'and'), ('FALSE', 'false'), ('OR', 'or'), ('@', '@'), ('ID', 'str'), ('DUBEQUAL', '=='), ('STRING', '"cool string"'), ('NEWLINE', '\n'), ('TRUE', 'true'), ('AND', 'and'), ('(', '('), ('FALSE', 'false'), ('OR', 'or'), ('@', '@'), ('ID', 'str'), ('DUBEQUAL', '=='), ('STRING', '"cool string"'), (')', ')'), ('NEWLINE', '\n')]

not_tokens = [('@', '@'), ('ID', 'myList'), ('=', '='), ('[', '['), ('NUMBER', '40'), (',', ','), ('NUMBER', '500'), (']', ']'), ('NEWLINE', '\n'), ('NOT', 'not'), ('NUMBER', '100'), ('LESSTHANEQ', '<='), ('@', '@'), ('ID', 'myList'), ('[', '['), ('NUMBER', '1'), (']', ']'), ('NEWLINE', '\n')]

selection_if_tokens = [('IF', 'if'), ('@', '@'), ('ID', 'x'), ('<', '<'), ('NUMBER', '1'), (':', ':'), ('NEWLINE', '\n'), ('INDENT', 'INDENT'), ('@', '@'), ('ID', 'y'), ('=', '='), ('NUMBER', '5'), ('NEWLINE', '\n'), ('DEDENT', 'DEDENT')]

selection_ifelse_tokens = [('IF', 'if'), ('@', '@'), ('ID', 'x'), ('>', '>'), ('NUMBER', '1'), ('AND', 'and'), ('@', '@'), ('ID', 'y'), ('GREATERTHANEQ', '>='), ('NUMBER', '1'), (':', ':'), ('NEWLINE', '\n'), ('INDENT', 'INDENT'), ('@', '@'), ('ID', 'y'), ('=', '='), ('@', '@'), ('ID', 'y'), ('-', '-'), ('NUMBER', '5'), ('NEWLINE', '\n'), ('DEDENT', 'DEDENT'), ('ELSE', 'else'), (':', ':'), ('NEWLINE', '\n'), ('INDENT', 'INDENT'), ('@', '@'), ('ID', 'y'), ('=', '='), ('NUMBER', '3'), ('NEWLINE', '\n'), ('DEDENT', 'DEDENT')]

iteraton_for_tokens = [('FOR', 'for'), ('@', '@'), ('ID', 'image'), ('IN', 'in'), ('@', '@'), ('ID', 'images'), (':', ':'), ('NEWLINE', '\n'), ('INDENT', 'INDENT'), ('@', '@'), ('ID', 'x'), ('=', '='), ('@', '@'), ('ID', 'x'), ('+', '+'), ('NUMBER', '1'), ('NEWLINE', '\n'), ('DEDENT', 'DEDENT')]

multiplicative_tokens = [('@', '@'), ('ID', 'x'), ('=', '='), ('@', '@'), ('ID', 'y'), ('*', '*'), ('NUMBER', '5'), ('NEWLINE', '\n'), ('@', '@'), ('ID', 'y'), ('=', '='), ('@', '@'), ('ID', 'x'), ('/', '/'), ('NUMBER', '5'), ('NEWLINE', '\n')]

equality_notequal_tokens = [('@', '@'), ('ID', 'test'), ('=', '='), ('(', '('), ('NUMBER', '5'), ('NEQUAL', '!='), ('NUMBER', '3'), (')', ')'), ('NEWLINE', '\n')]

color_setting_tokens = [('@', '@'), ('ID', 'red'), ('=', '='), ('ID', 'color'), ('(', '('), ('NUMBER', '0'), (',', ','), ('NUMBER', '0'), (',', ','), ('NUMBER', '0'), (')', ')'), ('NEWLINE', '\n'), ('@', '@'), ('ID', 'image1'), ('=', '='), ('@', '@'), ('ID', 'red') ]


'''
abstract syntax tress
'''


oneliner_tree = '[program [statement_list [statement [expression_statement [expression [assignment_expression [logical_OR_expression [logical_AND_expression [equality_expression [relational_expression [additive_expression [multiplicative_expression [logical_NOT_expression [intermediate_expression [function_expression [#] [grayscale] [parameters [primary_expression [variable_access_expression [variable_expression [@] [image1]]]]]]]]]]]]]]]] [\n]]]]]'

indent_tree = '[program [statement_list [statement_list [statement_list [statement [selection_statement [if] [expression [assignment_expression [logical_OR_expression [logical_AND_expression [equality_expression [relational_expression [relational_expression [additive_expression [multiplicative_expression [logical_NOT_expression [intermediate_expression [primary_expression [variable_access_expression [variable_expression [@] [hey]]]]]]]]] [<] [additive_expression [multiplicative_expression [logical_NOT_expression [not] [logical_NOT_expression [intermediate_expression [primary_expression [1]]]]]]]]]]]]] [block [:] [\n] [INDENT] [statement_list [statement [expression_statement [expression [assignment_expression [logical_OR_expression [logical_AND_expression [equality_expression [relational_expression [additive_expression [multiplicative_expression [logical_NOT_expression [intermediate_expression [function_expression [#] [sup] []]]]]]]]]]]] [\n]]]] [DEDENT]]]]] [statement [expression_statement [expression [assignment_expression [logical_OR_expression [logical_AND_expression [equality_expression [relational_expression [additive_expression [multiplicative_expression [logical_NOT_expression [intermediate_expression [function_expression [#] [hey] [parameters [primary_expression [variable_access_expression [variable_expression [@] [image1]]]]]]]]]]]]]]]] [\n]]]] [statement [iteration_statement [for] [variable_expression [@] [image]] [in] [primary_expression [variable_access_expression [variable_expression [@] [images]]]] [block [:] [\n] [INDENT] [statement_list [statement [selection_statement [if] [expression [assignment_expression [logical_OR_expression [logical_AND_expression [equality_expression [equality_expression [relational_expression [additive_expression [multiplicative_expression [logical_NOT_expression [intermediate_expression [primary_expression [variable_access_expression [variable_expression [@] [image]]]]]]]]]] [==] [relational_expression [additive_expression [multiplicative_expression [logical_NOT_expression [intermediate_expression [primary_expression [variable_access_expression [variable_expression [@] [image1]]]]]]]]]]]]]] [block [:] [\n] [INDENT] [statement_list [statement [expression_statement [expression [assignment_expression [logical_OR_expression [logical_AND_expression [equality_expression [relational_expression [additive_expression [multiplicative_expression [logical_NOT_expression [intermediate_expression [function_expression [#] [hey] [parameters [primary_expression [variable_access_expression [variable_expression [@] [image]]]]]]]]]]]]]]]] [\n]]]] [DEDENT]]]]] [DEDENT]]]]] [translation_unit [function_definition [hey] [parameter_declaration [variable_expression [@] [myImage]]] [block [:] [\n] [INDENT] [statement_list [statement_list [statement [selection_statement [if] [expression [assignment_expression [logical_OR_expression [logical_AND_expression [equality_expression [relational_expression [relational_expression [additive_expression [multiplicative_expression [logical_NOT_expression [intermediate_expression [primary_expression [variable_access_expression [variable_access_expression [variable_expression [@] [myImage]]] [.] [width]]]]]]]] [>] [additive_expression [multiplicative_expression [logical_NOT_expression [intermediate_expression [primary_expression [100]]]]]]]]]]]] [block [:] [\n] [INDENT] [statement_list [statement [selection_statement [if] [expression [assignment_expression [logical_OR_expression [logical_AND_expression [logical_AND_expression [equality_expression [relational_expression [relational_expression [additive_expression [multiplicative_expression [logical_NOT_expression [intermediate_expression [primary_expression [variable_access_expression [variable_access_expression [variable_expression [@] [myImage]]] [.] [height]]]]]]]] [>] [additive_expression [multiplicative_expression [logical_NOT_expression [intermediate_expression [primary_expression [50]]]]]]]]] [and] [equality_expression [relational_expression [relational_expression [additive_expression [multiplicative_expression [logical_NOT_expression [intermediate_expression [primary_expression [variable_access_expression [variable_access_expression [variable_expression [@] [myImage]]] [.] [height]]]]]]]] [<] [additive_expression [multiplicative_expression [logical_NOT_expression [intermediate_expression [primary_expression [60]]]]]]]]]]]] [block [:] [\n] [INDENT] [statement_list [statement_list [statement [expression_statement [expression [assignment_expression [variable_expression [@] [x]] [=] [assignment_expression [logical_OR_expression [logical_AND_expression [equality_expression [relational_expression [additive_expression [multiplicative_expression [logical_NOT_expression [intermediate_expression [primary_expression [10]]]]]]]]]]]]] [\n]]]] [statement [expression_statement [expression [assignment_expression [variable_expression [@] [y]] [=] [assignment_expression [logical_OR_expression [logical_AND_expression [equality_expression [relational_expression [additive_expression [multiplicative_expression [logical_NOT_expression [intermediate_expression [primary_expression [50]]]]]]]]]]]]] [\n]]]] [DEDENT]]]]] [DEDENT]] [else] [block [:] [\n] [INDENT] [statement_list [statement_list [statement [expression_statement [expression [assignment_expression [variable_expression [@] [x]] [=] [assignment_expression [logical_OR_expression [logical_AND_expression [equality_expression [relational_expression [additive_expression [multiplicative_expression [logical_NOT_expression [intermediate_expression [primary_expression [100]]]]]]]]]]]]] [\n]]]] [statement [expression_statement [expression [assignment_expression [variable_expression [@] [y]] [=] [assignment_expression [logical_OR_expression [logical_AND_expression [equality_expression [relational_expression [additive_expression [multiplicative_expression [logical_NOT_expression [intermediate_expression [primary_expression [20]]]]]]]]]]]]] [\n]]]] [DEDENT]]]]] [statement [return_statement [return] [expression_statement [expression [assignment_expression [logical_OR_expression [logical_AND_expression [equality_expression [relational_expression [additive_expression [multiplicative_expression [logical_NOT_expression [intermediate_expression [primary_expression [variable_access_expression [variable_expression [@] [x]]]]]]]]]]]]]] [\n]]]]] [DEDENT]]]]]'

function_def_tree = '[program [statement_list [statement [expression_statement [expression [assignment_expression [logical_OR_expression [logical_AND_expression [equality_expression [relational_expression [additive_expression [multiplicative_expression [logical_NOT_expression [intermediate_expression [function_expression [#] [sup] [parameters [parameters [primary_expression [variable_access_expression [variable_expression [@] [image1]]]]] [,] [primary_expression [variable_access_expression [variable_expression [@] [image2]]]]]]]]]]]]]]]] [\n]]]] [translation_unit [function_definition [sup] [parameter_declaration [parameter_declaration [variable_expression [@] [myImage1]]] [,] [variable_expression [@] [myImage2]]] [block [:] [\n] [INDENT] [statement_list [statement [return_statement [return] [expression_statement [expression [assignment_expression [logical_OR_expression [logical_AND_expression [equality_expression [relational_expression [additive_expression [additive_expression [multiplicative_expression [logical_NOT_expression [intermediate_expression [primary_expression [variable_access_expression [variable_access_expression [variable_expression [@] [myImage1]]] [.] [height]]]]]]] [+] [multiplicative_expression [logical_NOT_expression [intermediate_expression [primary_expression [variable_access_expression [variable_access_expression [variable_expression [@] [myImage2]]] [.] [height]]]]]]]]]]]]] [\n]]]]] [DEDENT]]]]]'

or_and_tree = '[program [statement_list [statement_list [statement [expression_statement [expression [assignment_expression [logical_OR_expression [logical_OR_expression [logical_AND_expression [logical_AND_expression [equality_expression [relational_expression [additive_expression [multiplicative_expression [logical_NOT_expression [intermediate_expression [primary_expression [true]]]]]]]]] [and] [equality_expression [relational_expression [additive_expression [multiplicative_expression [logical_NOT_expression [intermediate_expression [primary_expression [false]]]]]]]]]] [or] [logical_AND_expression [equality_expression [equality_expression [relational_expression [additive_expression [multiplicative_expression [logical_NOT_expression [intermediate_expression [primary_expression [variable_access_expression [variable_expression [@] [str]]]]]]]]]] [==] [relational_expression [additive_expression [multiplicative_expression [logical_NOT_expression [intermediate_expression [primary_expression ["cool string"]]]]]]]]]]]] [\n]]]] [statement [expression_statement [expression [assignment_expression [logical_OR_expression [logical_AND_expression [logical_AND_expression [equality_expression [relational_expression [additive_expression [multiplicative_expression [logical_NOT_expression [intermediate_expression [primary_expression [true]]]]]]]]] [and] [equality_expression [relational_expression [additive_expression [multiplicative_expression [logical_NOT_expression [intermediate_expression [primary_expression [(] [expression [assignment_expression [logical_OR_expression [logical_OR_expression [logical_AND_expression [equality_expression [relational_expression [additive_expression [multiplicative_expression [logical_NOT_expression [intermediate_expression [primary_expression [false]]]]]]]]]] [or] [logical_AND_expression [equality_expression [equality_expression [relational_expression [additive_expression [multiplicative_expression [logical_NOT_expression [intermediate_expression [primary_expression [variable_access_expression [variable_expression [@] [str]]]]]]]]]] [==] [relational_expression [additive_expression [multiplicative_expression [logical_NOT_expression [intermediate_expression [primary_expression ["cool string"]]]]]]]]]]]] [)]]]]]]]]]]]] [\n]]]]]'

not_tree = '[program [statement_list [statement_list [statement [expression_statement [expression [assignment_expression [variable_expression [@] [myList]] [=] [assignment_expression [logical_OR_expression [logical_AND_expression [equality_expression [relational_expression [additive_expression [multiplicative_expression [logical_NOT_expression [intermediate_expression [primary_expression [\\[] [parameters [parameters [primary_expression [40]]] [,] [primary_expression [500]]] [\\]]]]]]]]]]]]]] [\n]]]] [statement [expression_statement [expression [assignment_expression [logical_OR_expression [logical_AND_expression [equality_expression [relational_expression [relational_expression [additive_expression [multiplicative_expression [logical_NOT_expression [not] [logical_NOT_expression [intermediate_expression [primary_expression [100]]]]]]]] [<=] [additive_expression [multiplicative_expression [logical_NOT_expression [intermediate_expression [primary_expression [variable_access_expression [variable_access_expression [variable_expression [@] [myList]]] [\\[] [primary_expression [1]] [\\]]]]]]]]]]]]]] [\n]]]]]'

selection_if_tree = '[program [statement_list [statement [selection_statement [if] [expression [assignment_expression [logical_OR_expression [logical_AND_expression [equality_expression [relational_expression [relational_expression [additive_expression [multiplicative_expression [logical_NOT_expression [intermediate_expression [primary_expression [variable_access_expression [variable_expression [@] [x]]]]]]]]] [<] [additive_expression [multiplicative_expression [logical_NOT_expression [intermediate_expression [primary_expression [1]]]]]]]]]]]] [block [:] [\n] [INDENT] [statement_list [statement [expression_statement [expression [assignment_expression [variable_expression [@] [y]] [=] [assignment_expression [logical_OR_expression [logical_AND_expression [equality_expression [relational_expression [additive_expression [multiplicative_expression [logical_NOT_expression [intermediate_expression [primary_expression [5]]]]]]]]]]]]] [\n]]]] [DEDENT]]]]]]'

selection_ifelse_tree = '[program [statement_list [statement [selection_statement [if] [expression [assignment_expression [logical_OR_expression [logical_AND_expression [logical_AND_expression [equality_expression [relational_expression [relational_expression [additive_expression [multiplicative_expression [logical_NOT_expression [intermediate_expression [primary_expression [variable_access_expression [variable_expression [@] [x]]]]]]]]] [>] [additive_expression [multiplicative_expression [logical_NOT_expression [intermediate_expression [primary_expression [1]]]]]]]]] [and] [equality_expression [relational_expression [relational_expression [additive_expression [multiplicative_expression [logical_NOT_expression [intermediate_expression [primary_expression [variable_access_expression [variable_expression [@] [y]]]]]]]]] [>=] [additive_expression [multiplicative_expression [logical_NOT_expression [intermediate_expression [primary_expression [1]]]]]]]]]]]] [block [:] [\n] [INDENT] [statement_list [statement [expression_statement [expression [assignment_expression [variable_expression [@] [y]] [=] [assignment_expression [logical_OR_expression [logical_AND_expression [equality_expression [relational_expression [additive_expression [additive_expression [multiplicative_expression [logical_NOT_expression [intermediate_expression [primary_expression [variable_access_expression [variable_expression [@] [y]]]]]]]] [-] [multiplicative_expression [logical_NOT_expression [intermediate_expression [primary_expression [5]]]]]]]]]]]]] [\n]]]] [DEDENT]] [else] [block [:] [\n] [INDENT] [statement_list [statement [expression_statement [expression [assignment_expression [variable_expression [@] [y]] [=] [assignment_expression [logical_OR_expression [logical_AND_expression [equality_expression [relational_expression [additive_expression [multiplicative_expression [logical_NOT_expression [intermediate_expression [primary_expression [3]]]]]]]]]]]]] [\n]]]] [DEDENT]]]]]]'

iteration_for_tree = '[program [statement_list [statement [iteration_statement [for] [variable_expression [@] [image]] [in] [primary_expression [variable_access_expression [variable_expression [@] [images]]]] [block [:] [\n] [INDENT] [statement_list [statement [expression_statement [expression [assignment_expression [variable_expression [@] [x]] [=] [assignment_expression [logical_OR_expression [logical_AND_expression [equality_expression [relational_expression [additive_expression [additive_expression [multiplicative_expression [logical_NOT_expression [intermediate_expression [primary_expression [variable_access_expression [variable_expression [@] [x]]]]]]]] [+] [multiplicative_expression [logical_NOT_expression [intermediate_expression [primary_expression [1]]]]]]]]]]]]] [\n]]]] [DEDENT]]]]]]'

multiplicative_tree = '[program [statement_list [statement_list [statement [expression_statement [expression [assignment_expression [variable_expression [@] [x]] [=] [assignment_expression [logical_OR_expression [logical_AND_expression [equality_expression [relational_expression [additive_expression [multiplicative_expression [multiplicative_expression [logical_NOT_expression [intermediate_expression [primary_expression [variable_access_expression [variable_expression [@] [y]]]]]]] [*] [logical_NOT_expression [intermediate_expression [primary_expression [5]]]]]]]]]]]]] [\n]]]] [statement [expression_statement [expression [assignment_expression [variable_expression [@] [y]] [=] [assignment_expression [logical_OR_expression [logical_AND_expression [equality_expression [relational_expression [additive_expression [multiplicative_expression [multiplicative_expression [logical_NOT_expression [intermediate_expression [primary_expression [variable_access_expression [variable_expression [@] [x]]]]]]] [/] [logical_NOT_expression [intermediate_expression [primary_expression [5]]]]]]]]]]]]] [\n]]]]]'

equality_notequal_tree = '[program [statement_list [statement [expression_statement [expression [assignment_expression [variable_expression [@] [test]] [=] [assignment_expression [logical_OR_expression [logical_AND_expression [equality_expression [relational_expression [additive_expression [multiplicative_expression [logical_NOT_expression [intermediate_expression [primary_expression [(] [expression [assignment_expression [logical_OR_expression [logical_AND_expression [equality_expression [equality_expression [relational_expression [additive_expression [multiplicative_expression [logical_NOT_expression [intermediate_expression [primary_expression [5]]]]]]]] [!=] [relational_expression [additive_expression [multiplicative_expression [logical_NOT_expression [intermediate_expression [primary_expression [3]]]]]]]]]]]] [)]]]]]]]]]]]]] [\n]]]]]'

color_setting_tree = '[program [statement_list [statement [expression_statement [expression [assignment_expression [variable_expression [@] [test]] [=] [assignment_expression [logical_OR_expression [logical_AND_expression [equality_expression [relational_expression [additive_expression [multiplicative_expression [logical_NOT_expression [intermediate_expression [primary_expression [(] [expression [assignment_expression [logical_OR_expression [logical_AND_expression [equality_expression [equality_expression [relational_expression [additive_expression [multiplicative_expression [logical_NOT_expression [intermediate_expression [primary_expression [5]]]]]]]] [!=] [relational_expression [additive_expression [multiplicative_expression [logical_NOT_expression [intermediate_expression [primary_expression [3]]]]]]]]]]]] [)]]]]]]]]]]]]] [\n]]]]]'

'''
python strings
'''

oneliner_python = 'fixelFunctions.grayscale(ns.image1)\n'

indent_python = '''\
def hey(myImage):
	if myImage.width > 100:
		if myImage.height > 50 and myImage.height < 60:
			x = 10
			y = 50
	else:
		x = 100
		y = 20
	return x
if ns.hey < not 1:
	sup()
hey(ns.image1)
for ns.image in ns.images:
	if ns.image == ns.image1:
		hey(ns.image)
'''

function_def_python = '''\
def sup(myImage1, myImage2):
	return myImage1.height + myImage2.height
sup(ns.image1, ns.image2)
'''

or_and_python='''\
true and false or ns.str == "coolstring"
true and (false or ns.str == "coolstring")
'''

not_python='''\
ns.myList = [40, 500]
not 100 <= ns.myList[1]
'''

selection_if_python='''\
if ns.x < 1:
	ns.y = 5
'''

selection_ifelse_python='''\
if ns.x > 1 and ns.y >= 1:
	ns.y = ns.y - 5
else:
	ns.y = 3
'''

equality_notequal_python='''\
ns.test = (5 != 3)
'''

multiplicative_python='''\
ns.x = ns.y * 5
ns.y = ns.x / 5
'''

iteration_for_python='''\
for ns.image in ns.images:
	ns.x = ns.x + 1
'''

color_setting_python='''\
red = color(0,0,0)
image1[302,19] = red
'''
