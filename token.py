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
token=(
	'GT',
	
	)

#recognize the string and get the token
def token_recogn(lines):
