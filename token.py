import ply.lex as lex

#file input API
def read_token():
	with open(file,'r') as f:
		return f.readlines()

#the reserved keyword tuple
reserved={
	'function':'FUNC',
	'main':'MAIN',
	'while':'WHILE',
	'if':'IF',
	'else':'ELSE',
	'var':'VAR',
	'break':'BREAK'
}

#other token name
token=[
	'GT',#bigger 
	'LT',#littler
	'EQ',#equal
	'GTEQ',# be equal or greater than
	'LTEQ',# be litter or greater than
	'AND',#and
	'OR',#or
	'NOT'#not

	]+list(reserved.values())

#define the regluar
def t_main(t):
	r'main'
	t.value=int(t.value)
	return t
	
#build the lexer
lexer=lex.lex()
#recognize the string and get the token
#def token_recogn(lines):

lexer.input('main')

if __name__=='__main__':
	while True:
		tok=lexer.token()
		if not tok:break
		print tok	

http://www.pchou.info/open-source/2014/01/18/52da47204d4cb.html