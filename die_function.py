
from dieparser import parser
from dielexer import lexer


class DieFunction (object):
  def __init__(self, st):
    tokens = lexer.lex(st)
    nodes = parser.parse(tokens)

  def roll(self):
    pass

  # def get
  #   pass

  @property
  def value(self):
    pass
