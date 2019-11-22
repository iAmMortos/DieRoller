# import sharedlibs
# sharedlibs.add_path_for('dice')
# from die import Die
# from dice import Dice


class Parser(object):
  def __init__(self, exp):
    self._string_exp = exp

  @staticmethod
  def _get_precedence(op):
    if op in '+-':
      return 1
    if op in '*/':
      return 2
    return 0

  @staticmethod
  def _apply_op(a, b, op):
    if op == '+': return a + b
    if op == '-': return a - b
    if op == '*': return a * b
    if op == '/': return a // b

  @staticmethod
  def parse(tstr):
    # store integers
    values = []

    # store operators
    ops = []
    i = 0

    while i < len(tstr):
      # skip whitespace
      if tstr[i].strip() == '':
        i += 1
        continue

      # Current token is an opening paren, push to ops
      elif tstr[i] == '(':
        ops.append(tstr[i])

      # Current token is a number
      elif tstr[i].isdigit():
        val = 0
        # Grab more digits
        while i < len(tstr) and tstr[i].isdigit():
          val = val * 10 + int(tstr[i])
          i += 1
        values.append(val)

      # Closing paren, solve interior
      elif tstr[i] == ')':
        while len(ops) != 0 and ops[-1] != '(':
          v2 = values.pop()
          v1 = values.pop()
          op = ops.pop()
          values.append(Parser._apply_op(v1, v2, op))
        ops.pop()

      # Token is an operator
      else:
        # While top of 'ops' has same or greater precedence to current token, which is an operator,
        #  apply operator on top of 'ops' to top two elements in values stack
        while len(ops) > 0 and Parser._get_precedence(ops[-1]) >= Parser._get_precedence(tstr[i]):
          v2 = values.pop()
          v1 = values.pop()
          op = ops.pop()
          values.append(Parser._apply_op(v1, v2, op))
        ops.append(tstr[i])

      i += 1

    # Entire expression has been parsed, apply remaining ops to remaining values in stacks
    while len(ops) > 0:
      v2 = values.pop()
      v1 = values.pop()
      op = ops.pop()
      values.append(Parser._apply_op(v1, v2, op))

    return values[-1]


if __name__ == '__main__':
  print(Parser.parse('10 + 2 * 6'))
  print(Parser.parse('100 * 2 + 12'))
  print(Parser.parse('100 * ( 2 + 12 )'))
  print(Parser.parse('100 * ( 2 + 12 ) / 14'))
  print(Parser.parse('10 * ( 5 + ( 4 / 2 ) )'))
