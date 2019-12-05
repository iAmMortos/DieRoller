
from lexer.token_type import TokenType

class ParseNode (object):
	def __init__(self, node_type):
		self.type = node_type
		self.a = None
		self.b = None
		self.op = None
		self._value = None
		
	@property
	def value(self):
		if self._value == None:
			if self.type == TokenType.
		return self._value
