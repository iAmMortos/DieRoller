
from dielexer.token_type import TokenType
from dieparser.parse_node import ParseNode


def get_precedence(op):
  if op in '*/':
    return 2
  if op in '+-':
    return 1
  return 0


def parse(tokens):
  nodes = []
  ops = []
  i = 0
  while i < len(tokens):
    if tokens[i].type == TokenType.PAREN and tokens[i].value == '(':
      ops.append(tokens[i].value)
    elif tokens[i].type == TokenType.CONST:
      nodes.append(ParseNode(TokenType.CONST, tokens[i].value))
    elif tokens[i].type == TokenType.DIE:
      nodes.append(ParseNode(TokenType.DIE, tokens[i].num, tokens[i].sides))
    elif tokens[i].type == TokenType.MATH_OP:
      pass
    i += 1

  return nodes.pop()