
class BinarySearchTree:
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None

	def add_child(self, data):
		if data == self.data:
			return

		if data < self.data:
			if self.left:
				self.left.add_child(data)
			else:
				self.left = BinarySearchTree(data)

		if data > self.data:
			if self.right:
				self.right.add_child(data)
			else:
				self.right = BinarySearchTree(data)

	def search(self, value):

		if value == self.data:
			return True

		if value < self.data:
			if self.left:
				return self.left.search(value)
			else:
				return False
		else:
			if self.right:
				return self.right.search(value)
			else:
				return False

	def in_order_traversal(self):
		
		elements = []

		if self.left:
			elements += self.left.in_order_traversal()

		elements.append(self.data)

		if self.right:
			elements += self.right.in_order_traversal()

		return elements

	def find_min(self):

		if self.left == None:
			return self.data

		return self.left.find_min()

	def find_max(self):

		if self.right == None:
			return self.data

		return self.right.find_max()

	def calculate_sum(self):

		left_sum = self.left.calculate_sum() if self.left else 0
		right_sum = self.right.calculate_sum() if self.right else 0
		
		return self.data + left_sum + right_sum

	def post_order_traversal(self):

		elements = []

		if self.left:
			elements += self.left.post_order_traversal()

		if self.right:
			elements += self.right.post_order_traversal()

		elements.append(self.data)

		return elements

	def pre_order_traversal(self):

		elements = [self.data]

		if self.left:
			elements += self.left.pre_order_traversal()

		if self.right:
			elements += self.right.pre_order_traversal()

		return elements



def build_tree(elements):

	print('Building tree out of the provided elements: ', elements)
	root = BinarySearchTree(elements[0])

	for i in range(1, len(elements)):
		root.add_child(elements[i])

	return root

if __name__ == '__main__':
	numbers = [15,12,7,14,27,20,23,88]

	numbers_tree = build_tree(numbers)
	print("Input numbers:",numbers)
	print("Min:",numbers_tree.find_min())
	print("Max:",numbers_tree.find_max())
	print("Sum:", numbers_tree.calculate_sum())
	print("In order traversal:", numbers_tree.in_order_traversal())
	print("Pre order traversal:", numbers_tree.pre_order_traversal())
	print("Post order traversal:", numbers_tree.post_order_traversal())



