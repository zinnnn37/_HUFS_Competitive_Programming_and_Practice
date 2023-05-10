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

	def add(self, val, parent=None):
		node = Node(val)
		if parent == None:
			self.root = node
			self.size += 1
		else:
			parent_node = self.search_node(self.root, parent)
			parent_node.child.append(node)
			self.size += 1


def _preorder(pre, node):
	if node == None:
		return
	pre.append(node.val)
	for child in node.child:
		_preorder(pre, child)
	return pre

def preorder(root):
	pre = []
	return _preorder(pre, root)

def _postorder(post, node):
	if node == None:
		return
	for child in node.child:
		_postorder(post, child)
	post.append(node.val)
	return post

def postorder(root):
	post = []
	return _postorder(post, root)

def query_ancestor(a, b):
	if pre.index(a) > pre.index(b):
		return False
	if post.index(a) < post.index(b):
		return False
	return True

if __name__ == '__main__':
	tree = Tree()
	tree.add(1)

	n, q = map(int, input().split())
	for _ in range(n-1):
		p, c = map(int, input().split())
		tree.add(c, p)

	pre = preorder(tree.root)
	post = postorder(tree.root)

	cnt = 0
	for _ in range(q):
		a, b = map(int, input().split())
		if (query_ancestor(a, b)):
			cnt += 1
	print(cnt)

# 엥 이것도 런타임 에러.. 심지어 9, 10번 타임아웃