import parser
import lexer
import generator


def translate(source):
    my_lex = lexer.get_lex()
    my_parser = parser.get_yacc()

    tree = my_parser.parse(source, lexer=my_lex)

    gen = generator.Generator(tree)
    return gen.get_string()
