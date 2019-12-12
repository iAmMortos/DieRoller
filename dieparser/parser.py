
from dielexer.token_type import TokenType


def parse(tokens):
  nodes = []
  ops = []
  i = 0
  while i < len(tokens):
    if tokens[i].value == '(':
      ops.append(tokens[i].value)
    elif tokens[i].type in [TokenType.DIE, TokenType.CONST]:
      nodes.append(tokens[i])
    i += 1

  return nodes