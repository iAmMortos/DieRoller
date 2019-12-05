
import random
from die.roll_result import RollResult

class Die (object):
  def __init__(self, sides):
    self.sides = sides
    self.value = sides
    self.result = None

  def _get_random_value(self):
    return random.randint(1, self.sides)

  def roll(self):
    self.value = self._get_random_value()
    self.result = RollResult([self.value], self.value)
    return self.value

  def roll_with_advantage(self):
    r1 = self._get_random_value()
    r2 = self._get_random_value()
    v = max(r1, r2)
    self.result = RollResult([r1, r2], v)
    self.value = v
    return v

  def roll_with_disadvantage(self):
    r1 = self._get_random_value()
    r2 = self._get_random_value()
    v = min(r1, r2)
    self.result = RollResult([r1, r2], v)
    self.value = v
    return v

  @property
  def min_value(self):
    return 1

  @property
  def max_value(self):
    return self.sides
