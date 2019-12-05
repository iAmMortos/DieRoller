
class LocationalError(Exception):
	def __init__(self, message, code, pos):
		ptr = ' '*pos + '^'
		m = '{}\n{}\n{}'.format(message, code, ptr)
		super().__init__(m)
