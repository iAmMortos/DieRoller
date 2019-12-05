from dielexer import lexer
from dieparser.parse_node import ParseNode
from dielexer.token_type import TokenType

def _parse_tokens(tokens):
	nodes = []
	ops = []
	i = 0
	while i < len(tokens):
		if tokens[i].value == '(':
			ops.append(tokens[i].value)
		elif tokens[i].type in [TokenType.DIE, TokenType.CONST]:
			nodes.append(tokens[i])
		i += 1

def parse(st):
	tokens = lexer.lex(st)
	return _parse_tokens(tokens)
