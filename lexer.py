
# reserved words that translate straight to tokens
reserved = {
  'for'   : 'FOR',
  'while' : 'WHILE',
  'if'    : 'IF',
  'else'  : 'ELSE',
  'return': 'RETURN',
  'in'    : 'IN',
  'true'  : 'TRUE',
  'false' : 'FALSE',
  'and'   : 'AND',
  'or'    : 'OR',
  'not'   : 'NOT',
}

# a list of all tokens produced by the lexer
tokens = [
    'ID','NUMBER',
    'PLUS','MINUS','TIMES','DIVIDE','EQUALS',
    'LPAREN','RPAREN','COMMENT','LBRACK','RBRACK',
    'COLON','COMMA', 'HASH','AT','LESSTHANEQ',
    'GREATERTHANEQ', 'LESSTHAN', 'GREATERTHAN', 'NEQUAL',
    'STRING','NEWLINE','INDENT',
    ] + list(reserved.values())

# Tokens produced by simple regexes
t_PLUS        = r'\+'
t_MINUS       = r'-'
t_TIMES       = r'\*'
t_COMMENT     = r'//'
t_DIVIDE      = r'/'
t_EQUALS      = r'='
t_LPAREN      = r'\('
t_RPAREN      = r'\)'
t_LBRACK      = r'\['
t_RBRACK      = r'\]'
t_COLON       = r':'
t_COMMA       = r','
t_STRING      = r'\"([^"])*\"'
t_HASH        = r'\#'
t_AT          = r'@'
t_LESSTHANEQ  = r'<='
t_GREATERTHANEQ = r'>='
t_LESSTHAN    = r'<'
t_GREATERTHAN = r'>'
t_NEQUAL      = r'!='
t_NEWLINE     = r'\n'
t_INDENT      = r'\t'
t_ID    = r'[a-zA-Z_][a-zA-Z0-9_]*'

# produces a token for any integer number and stores the value as an int
def t_NUMBER(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print("Integer value too large %d", t.value)
        t.value = 0
    return t

# Ignored characters
t_ignore = " "

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)
    
# Build the lexer
import ply.lex as lex
lexer = lex.lex()

## feed it some input data - test - how do we automate this?
data = '''
@desiredWidth = @image1.width*2
@desiredHeight = @image1.height*2
@imagesToStandardize = [@image2,@image3]

for @currentImage in @imagesToStandardize:
    #stretch @desiredWidth, @desiredHeight, @currentImage
'''

# give the lexer some input
lexer.input(data)

#tokenize
while True:
  tok = lexer.token()
  if not tok: break #no more input
  print tok
