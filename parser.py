import sharedlibs
sharedlibs.add_path_for('dice')
from die import Die
from dice import Dice


class Parser (object):
	def __init__(self, exp):
		self._string_exp = exp


if __name__ == '__main__':
	pass
