import sys
class node:
	def __init__(self,key):
		self.val = key
		self.left = None
		self.right = None
def insert(root,node):
	if root is None:
		root = node
	else:
		if node.val > root.val:
			if root.right is None:
				root.right = node
			else:
				insert(root.right,node)
		else:
			insert(root.left,node)
def inorder(root):
	if root:
		inorder(root.left)
		print(root.val)
		inorder(root.right)

def preorder(root):
	if root:
		print(root.val)
		preorder(root.left)
		preorder(root.right)

def postorder(root):
	if root:
		postorder(root.left)
		postorder(root.right)
		print(root.val)
def search(root,key):
	if root is None or root.val == key:
		return root
	if key > root.val:
		return search(root.right,key)
	return search(root.left,key)
n = list(map(int,input('enter number separated by space').split(' ')))
root = node(n[0])
n.pop(0)
for i in n:
        new_node = node(i)
        insert(root,new_node)
print('tree created')
action = input('preorder||postorder||inorder||search')
if action == 'preorder':
	print(preorder(root))
elif action == 'inorder':
	print(inorder(root))
elif action == 'postorder':
	print(postorder(root))
elif action == 'search':
	search_element = int(input('enter the search_element'))
	print(search(root,search_element))
else:
	print('no action')

