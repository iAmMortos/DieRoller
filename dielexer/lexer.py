
from dielexer.token_type import TokenType
from dielexer.d_token import Token
from dielexer.d_const_token import ConstToken
from dielexer.d_die_token import DieToken
from dieerrors.paren_mismatch_error import ParenMismatchError

def lex(st):
	i = 0
	open_parens = 0
	tokens = []
	while i < len(st):
		c = st[i]
		
		if c in '()':
			if c == '(':
				open_parens += 1
			else:
				open_parens -= 1
				if open_parens < 0:
					raise ParenMismatchError(st, i)
			tokens.append(Token(TokenType.PAREN, c))
		elif c in '+-*/':
			tokens.append(Token(TokenType.MATH_OP, c))
		elif c.isdigit():
			v = 0
			while i < len(st) and st[i].isdigit():
				v = v * 10 + int(st[i])
				i += 1
			if i + 1 < len(st) and st[i].lower() == 'd':
				# die notation maybe
				i += 1
				if not st[i].isdigit():
					raise Exception('Invalid die notation at %s' % i)
				v2 = 0
				while i < len(st) and st[i].isdigit():
					v2 = v2 * 10 + int(st[i])
					i += 1
				tokens.append(DieToken(v, v2))
			else:
				# const
				tokens.append(ConstToken(v))
				
			# move caret back one, will be moved automatically
			i -= 1
		elif c.strip() == '':
			# whitespace, skip
			pass
		
		i += 1
	if open_parens != 0:
		raise ParenMismatchError(st, i)
	return tokens
