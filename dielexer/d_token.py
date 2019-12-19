class Token (object):
	def __init__(self, t_type, value=None):
		self.type = t_type
		self.value = value
	def __repr__(self):
		return '[{}]\t{}'.format(self.type.name, self.value)
