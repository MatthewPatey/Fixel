# reserved words that translate straight to tokens
import re

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
	('dedentCount','inclusive'),
)

literals = ['#', '@', '+', '-', '*', '/', '=', '(', ')', 
            '[', ']', ':', ';', '<', '>' ]
            
globalIndent = 0
currentIndent = 0
auxIndent = 0

# a list of all tokens produced by the lexer
tokens = [
    'ID','NUMBER',
    'COMMENT',
    'LESSTHANEQ',
    'GREATERTHANEQ', 'NEQUAL',
    'STRING','NEWLINE','INDENT', 'EOF', 'DUBEQUAL', 'DEDENT'
    ] + list(reserved.values())

# Tokens produced by simple regexes
t_COMMENT     = r'//'
t_STRING      = r'\"([^"])*\"'
t_DUBEQUAL   = r'=='
t_LESSTHANEQ  = r'<='
t_GREATERTHANEQ = r'>='
t_NEQUAL      = r'!='
t_NEWLINE     = r'\r?\n'
t_ID    = r'[a-zA-Z_][a-zA-Z0-9_]*' 

# produces a token for any integer number and stores the value as an int
def t_NUMBER(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print("Integer value too large %d", t.value)
        t.value = 0
	#print "t_number"
    return t

# Ignored characters
t_ignore = " "

# count number of indents
def t_INDENT(t):
	r'^[\t]+'
	global globalIndent
	global currentIndent
	global auxIndent
	#print "t_indent"
	currentIndent = t.value.count("\t")
	if currentIndent < (globalIndent+auxIndent):
		if ((globalIndent+auxIndent)-currentIndent)>1:
			t.lexer.begin('dedentCount')
		else:
			t.type = "DEDENT"
			globalIndent=globalIndent-1
			return t
	elif currentIndent > (globalIndent+auxIndent):
		t.type = "INDENT"
		#auxIndent = currentIndent-globalIndent-1-auxIndent
		globalIndent=globalIndent+1
		return t

def t_dedentCount_empty(t):
	r'[ \t]*(?=[^ \t\r\n])'
	global globalIndent
	print "t_dedentCount_empty"
	global currentIndent
	global auxIndent
	if (globalIndent > currentIndent):
		#print "here"
		t.type = "DEDENT"
		t.value = globalIndent
		globalIndent=globalIndent-1
		return t
	else:
		#print t
		t.lexer.begin('INITIAL')

def t_lastDEDENT(t):
	r'\n(?=[^ \t\r\n])'
	global globalIndent
	global currentIndent
	global auxIndent
	auxIndent=0; 
	print "here"
	currentIndent=0
	#t.type="NEWLINE"
	if (globalIndent != 0):
		t.type="NEWLINE"
		#print "if"
		t.lexer.begin('dedentCount')
		return t;
	else:
		#print "else"
		t.type="NEWLINE"
		return t;
		
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


# Build the lexer
import ply.lex as lex

def get_lex():
    return lex.lex(reflags=re.MULTILINE)

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

