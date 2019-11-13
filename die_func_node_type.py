
from enum import Enum


class DieFuncNodeType(Enum):
  parenthesis = 0
  multiply = 1
  divide = 2
  add = 3
  subtract = 4
  negative = 5
  die = 6
  const = 7