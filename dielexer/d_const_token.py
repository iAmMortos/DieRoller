
from dielexer.token_type import TokenType
from dielexer.d_token import Token

class ConstToken (Token):
	def __init__(self, value):
		super().__init__(TokenType.CONST, value)
