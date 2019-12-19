
from dielexer.token_type import TokenType

class ParseNode (object):
	def __init__(self, node_type, a, b=None, op=None):
		self.type = node_type
		self.a = a
		self.b = b
		self.op = op
		self._value = None
		
	@property
	def value(self):
		if self._value is None:
			if self.type in [TokenType.PAREN, TokenType.DIE]:
				self._value = self.a.value
			elif self.type == TokenType.CONST:
				self._value = self.a
			elif self.type == TokenType.MATH_OP:
				if self.op == '+':
					return self.a.value + self.b.value
				elif self.op == '-':
					return self.a.value - self.b.value
				elif self.op == '*':
					return self.a.value * self.b.value
				elif self.op == '/':
					return self.a.value // self.b.value
		return self._value

	def get_formula_repr(self):
		if self.type == TokenType.PAREN:
			return '(%s)' % self.a.get_formula_repr()
		elif self.type == TokenType.CONST:
			return '%s' % self.a
		elif self.type == TokenType.DIE:
			return '%sd%s' % (self.a, self.b)
