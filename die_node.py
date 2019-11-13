from die_func_node import DieFuncNode
from die_func_node_type import DieFuncNodeType


class DieNode (DieFuncNode):
	def __init__(self):
		super().__init__()
		self.type = DieFuncNodeType.die
