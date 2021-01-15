class Node:
	def __init__(self, data=None, next=None):
		self.data = data
		self.next = next

class LinkedList:
	def __init__(self):
		self.head = None

	def insert_at_beginning(self, data):
		# the next element of my node will be the current head
		node = Node(data=data, next=self.head) 
		# once the node is created then my head now is the node
		self.head = node

	def print(self):
		if self.head is None:
			print('This is an empty LinkedList')
			return

		itr = self.head
		llstr = ''

		while itr:
			llstr += str(itr.data) + '--->'
			itr = itr.next
		print(llstr)

	def insert_at_end(self, data):
		# if the linked list is empty
		if self.head is None:
			# then we place the value and the next is none because its the last element of the list
			self.head = Node(data, None)
			return

		itr = self.head
		# while the next argument of the itr is not none (so its is not the last element)
		while itr.next:
			itr = itr.next

		# when itr.next becomes None then I am at the last element before adding the new one
		# when I am at the last element I want to point it out to the new element that I will
		# add after that (the new last element)

		itr.next = Node(data, None)

	def insert_values(self, data_list):
		self.head = None
		for data in data_list:
			self.insert_at_end(data)

	def get_length(self):
		count = 0 
		itr = self.head
		while itr:
			count += 1
			itr = itr.next
		return count

	def remove_at(self, index):
		# I cannot remove these indexes
		if index < 0 or index >= self.get_length():
			raise Exception('Invalid Index')

		# if i want to remove the first element of the linked list then i point the head to the next element
		if index == 0:
			self.head = self.head.next

		count = 0
		itr = self.head
		while itr:
			if count == index - 1:
				# when I reach one index before the one that I want to remove from my linked list
				# I point the next argument to the next of the next. Basically I skip the next element.
				itr.next = itr.next.next
				break

			itr = itr.next
			count += 1

	def insert_at(self, index, data):
		if index < 0 or index > self.get_length():
			raise Exception('Invalid Index')

		if index == 0:
			self.insert_at_beginning(data)

		count = 0
		itr = self.head
		while itr:
			if count == index-1:
				node = Node(data, itr.next)
				itr.next = node
				break

			itr = itr.next
			count += 1

	def insert_after_value(self, data_after, data_to_insert):
		# Search for first occurance of data_after value in linked list
		# Now insert data_to_insert after data_after node
		if self.head == None:
			return

		if self.head.data == data_after:
			self.head.next = Node(data_to_insert, self.head.next)

		itr = self.head
		while itr:
			if itr.data == data_after:
				node = Node(data_to_insert, itr.next)
				itr.next = node
				break
			itr = itr.next

	def remove_by_value(self, data):
		# Remove first node that contains data

		if self.head is None:
			return

		if self.head.data == data:
			self.head = self.head.next
			return

		itr = self.head
		while itr.next:
			if itr.next.data == data:
				itr.next = itr.next.next
				break
			itr = itr.next


if __name__ == '__main__':
	ll = LinkedList()
	ll.insert_values(["banana","mango","grapes","orange"])
	ll.print()
	ll.insert_after_value("mango","apple") # insert apple after mango
	ll.print()
	ll.remove_by_value("orange") # remove orange from linked list
	ll.print()
	ll.remove_by_value("banana")
	ll.print()
	ll.remove_by_value("mango")
	ll.print()
	ll.remove_by_value("apple")
	ll.print()
	ll.remove_by_value("grapes")
	ll.print()




		