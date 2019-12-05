from dieerrors.locational_error import LocationalError

class ParenMismatchError (LocationalError):
	def __init__(self, code, pos):
		super().__init__('Parenthesis did not match properly.', code, pos)
