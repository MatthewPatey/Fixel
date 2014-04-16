
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

literals = ['#', '@', '+', '-', '*', '/', '=', '(', ')', 
            '[', ']', ':', ';', '<', '>' ]
            
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
    return t

# Ignored characters
t_ignore = " "

# count number of indents
def t_INDENT(t):
	r'[\t]*'
	value = t.value.count("\t")
	global currentIndent
	global auxIndent
	if value < (currentIndent+auxIndent):
		if ((currentIndent+auxIndent)-value)>1:
			pass
		else:
			t.type = "DEDENT"
			currentIndent=currentIndent-1
			return t
	elif value > (currentIndent+auxIndent):
		t.type = "INDENT"
		auxIndent = value-currentIndent-1-auxIndent
		currentIndent=currentIndent+1
		return t
		
	
			
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)
    
# Build the lexer
import ply.lex as lex

lexer = lex.lex()


# Test it out
data = '''
#grayscale
		@image1
			#grayscale
@image	
'''

# Give the lexer some input
lexer.input(data)

# Tokenize
while True:
    tok = lexer.token()
    if not tok: break      # No more input
    print tok
