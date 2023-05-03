import sys
input = lambda: sys.stdin.readline().rstrip()

class Node:
	def __init__(self, val):
		self.val = val
		self.child = []

class Tree:
	def __init__(self):
		self.root = None
		self.size = 0

	def search_node(self, node, val):
		if node == None or node.val == val:
			return node
		for child in node.child:
			res = self.search_node(child, val)
			if res:
				return res
		return None