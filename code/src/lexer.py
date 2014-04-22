import ply.lex as lex
import re


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

# declare new state for dedent analysis
states = (
	('dedentCount', 'exclusive'),
    ('leadingWhitespace', 'inclusive'),
	('eofDedent', 'exclusive')
)

literals = ['#', '@', '+', '-', '*', '/', '=', '(', ')', 
            '[', ']', ':', ';', '<', '>', ',']
            
globalIndent = 0
currentIndent = 0

# a list of all tokens produced by the lexer
tokens = [
    'ID','NUMBER',
    'COMMENT',
    'LESSTHANEQ',
    'GREATERTHANEQ', 'NEQUAL',
    'STRING','NEWLINE','INDENT', 'DUBEQUAL', 'DEDENT'
    ] + list(reserved.values())

# Tokens produced by simple regexes
t_COMMENT     = r'//'
t_STRING      = r'\"([^"])*\"'
t_DUBEQUAL   = r'=='
t_LESSTHANEQ  = r'<='
t_GREATERTHANEQ = r'>='
t_NEQUAL      = r'!='
t_NEWLINE     = r'\r?\n'

# drop blank lines
def t_blankline(t):
	r'^[ \t]*\r?\n'
	pass

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    if t.value in reserved:
        t.type = reserved[t.value]
    return t

# produces a token for any integer number and stores the value as an int
def t_NUMBER(t):
    r'\d+'
    try:
        int(t.value)
    except ValueError:
        print("Integer value too large %d", t.value)
        t.value = 0
    return t

# Ignored characters
t_ignore = " "

# count number of indents
def t_INDENT(t):
	r'^[\t]+(?=[^ \t\r\n])'
	global globalIndent
	global currentIndent
	currentIndent = t.value.count("\t")
	if currentIndent < globalIndent:
		if (globalIndent-currentIndent) > 1:
			t.lexer.begin('dedentCount')
		else:
			t.value = t.type = "DEDENT"
			globalIndent = currentIndent
			return t
	elif currentIndent > globalIndent:
		t.value = t.type = "INDENT"
		if globalIndent == 0:
			t.lexer.begin('leadingWhitespace')
		globalIndent += 1
		return t

# match anything without consuming, keep returning DEDENT's until we've balanced
def t_dedentCount_empty(t):
	r'(?=.|\n)'
	global globalIndent
	global currentIndent
	if (globalIndent > currentIndent):
		t.value = t.type = "DEDENT"
		globalIndent -= 1
		return t
	else:
		if globalIndent > 0:
			t.lexer.begin('leadingWhitespace')
		else:
			t.lexer.begin('INITIAL')

def t_leadingWhitespace_EOF(t):
	r'\r?\n\Z'
	t.lexer.lexpos -= 1  # rollback lexpos so there's something to match for subsequent DEDENT's
	t.lexer.begin('eofDedent')
	t.type = 'NEWLINE'
	return t

def t_leadingWhitespace_leftmostDEDENT(t):
	r'^(?=[^ \t\r\n])'
	global currentIndent
	currentIndent = 0
	t.lexer.begin('dedentCount')

def t_eofDedent_DEDENT(t):
	r'(?=.|\n)'
	global globalIndent
	if globalIndent > 0:
		globalIndent -= 1
		t.type = t.value = 'DEDENT'
		return t
	else:
		t.lexer.lexpos += 1  # undo rollback so we don't consume last \n twice


def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


# Build the lexer

class VerboseLexer:
    def __init__(self, lex):
        self.lex = lex

    def token(self):
        """
        function that is dynamically added as instance method of an instance of the VerboseLexer class that is
        created at runtime if a verbose lexer is created. Returns one token from the lexer,
        but first prints it if it is not None.
        """
        token = self.lex.token()
        if token is not None:
            print(token)
        return token

    def input(self, data):
        self.lex.input(data)


def get_lex(verbose=False):
    """
    If verbose is false or omitted returns an instance of ply.lex created with lex rules in this module.
    If verbose is true, returns a wrapper around a lex instance that prints tokens before returning them.
    This distinction should be transparent to yacc.
    """
    my_lex = lex.lex(reflags=re.MULTILINE)

    if verbose:  # creates a wrapper around the lexer that prints tokens
        verbose_lexer = VerboseLexer(my_lex)
        return verbose_lexer
    else:
        return my_lex

'''
lexer = lex.lex(reflags=re.MULTILINE)
data=
@image1
@image
	#grayscale1
	#grayscale
		#grayscale2
	@image2
#grayscale3
	@image3
		#grayscale4
@image4
@image5


lexer.input(data)
#tokenize
while True:
	tok = lexer.token()
	if not tok: break
	print tok
'''

