import parser
import lexer
import generator


def translate(source_string=None, verbose=False):
    my_lex = lexer.get_lex(verbose)
    my_parser = parser.get_yacc()

    if source_string is None:
        source_string = 'if @hey:\n\t#sup\n'

    if verbose:
        print("source:\n")
        print(source_string + '\n')
        print('tokens:\n')

    tree = my_parser.parse(source_string, lexer=my_lex)
    gen = generator.Generator(tree)
    python_string = gen.get_string()

    if verbose:
        print("\nAST:\n")
        print(str(tree) + '\n')
        print('python:\n')

    print(python_string)
    return python_string
