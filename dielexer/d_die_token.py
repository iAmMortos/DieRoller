
from dielexer.d_token import Token
from dielexer.token_type import TokenType

class DieToken (Token):
	def __init__(self, num, sides):
		super().__init__(TokenType.DIE)
		self.num = num
		self.sides = sides
		self.value = '%sd%s' % (num, sides)
