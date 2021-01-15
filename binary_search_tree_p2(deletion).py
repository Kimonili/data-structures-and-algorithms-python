
class BinarySearchTreeNode:
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None

	def add_child(self, data):
		if data == self.data:
			return # node already exist

		if data < self.data:
			if self.left:
				self.left.add_child(data)
			else:
				self.left = BinarySearchTreeNode(data)
		else:
			if self.right:
				self.right.add_child(data)
			else:
				self.right = BinarySearchTreeNode(data)


	def search(self, val):
		if self.data == val:
			return True

		if val < self.data:
			if self.left:
				return self.left.search(val)
			else:
				return False

		if val > self.data:
			if self.right:
				return self.right.search(val)
			else:
				return False

	def pre_order_traversal(self):

		elements = [self.data]

		if self.left:
			elements += self.left.pre_order_traversal()

		if self.right:
			elements += self.right.pre_order_traversal()

		return elements

	def in_order_traversal(self):

		elements = []
		if self.left:
			elements += self.left.in_order_traversal()

		elements.append(self.data)

		if self.right:
			elements += self.right.in_order_traversal()

		return elements

	def delete(self, val):

		# if self.data is None:
		#     return None

		if val < self.data:
			if self.left:

				self.left = self.left.delete(val)

		elif val > self.data:
			# if the right branch of the current node exists 
			if self.right:
				# call the delete function recursively
				self.right = self.right.delete(val)

		else:
			# if the value to be deleted is a leaf node
			if self.left is None and self.right is None:
				return None

			# if the value to be deleted has a child on the right
			elif self.left is None:
				# return the left child
				return self.right

			# if the value to be deleted has a child on the left
			elif self.right is None:
				# return the left child
				return self.left

			# if nothing of the above is True, it means that the 
			# value to be deleted has two children

			# find the minimum value of the tight sub-tree of the 
			# value to be deleted
			min_val = self.right.find_min()
			# copy this minimum value to the current node (to the 
			# value that we want to delete)
			self.data = min_val
			self.right = self.right.delete(min_val)

		# return the root of the tree
		return self

	def find_max(self):
		if self.right is None:
			return self.data
		return self.right.find_max()

	def find_min(self):
		if self.left is None:
			return self.data
		return self.left.find_min()


def build_tree(elements):
	print("Building tree with these elements:",elements)
	root = BinarySearchTreeNode(elements[0])

	for i in range(1,len(elements)):
		root.add_child(elements[i])

	return root

if __name__ == '__main__':
	numbers_tree = build_tree([17, 4, 1, 20, 9, 23, 18, 34, 22])
	print("Before deleting 20 the in order traversal is: ",numbers_tree.in_order_traversal())
	print(numbers_tree.delete(20).data)
	print("After deleting 20 the in order traversal is: ",numbers_tree.in_order_traversal()) # this should print [1, 4, 9, 17, 18, 23, 34]

	# numbers_tree = build_tree([17, 4, 1, 20, 9, 23, 18, 34])
	# numbers_tree.delete(9)
	# print("After deleting 9 ",numbers_tree.in_order_traversal())  # this should print [1, 4, 17, 18, 20, 23, 34]

	# numbers_tree = build_tree([17, 4, 1, 20, 9, 23, 18, 34])
	# numbers_tree.delete(17)
	# print("After deleting 17 ",numbers_tree.in_order_traversal())  # this should print [1, 4, 9, 18, 20, 23, 34]