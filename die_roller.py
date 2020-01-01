
from die_function import DieFunction
from dielexer import lexer


def main():
	fn = DieFunction("2d8 * 1d12 + 3d6 / 2 - 4d4 * (2d6 * (5d20 - 4)) / 3")
	print('done')


if __name__ == '__main__':
	main()
