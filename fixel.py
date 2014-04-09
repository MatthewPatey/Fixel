from src import parser
from src import lexer
from src import generator


def main():
    my_lex = lexer.get_lex()
    my_parser = parser.get_yacc()

    ## feed it some input data - test - how do we automate this?
    data = '#grayscale @image1\n' #todo can we avoid requiring newline?

    tree = my_parser.parse(data, lexer=my_lex)
    print("I made a tree! yay!")
    print(tree)

    gen = generator.Generator(tree)
    print gen.get_string()


if __name__ == '__main__':
    main()
