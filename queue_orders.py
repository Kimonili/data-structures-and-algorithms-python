from collections import deque
import time
import threading

class Queue:
	
	def __init__(self):
		self.buffer = deque()
	
	def enqueue(self, val):
		self.buffer.appendleft(val)
		
	def dequeue(self):
		return self.buffer.pop()
	
	def is_empty(self):
		return len(self.buffer)==0
	
	def size(self):
		return len(self.buffer)



if __name__ == '__main__':

	def place_order(orders):
		for order in orders:
			print("Placing the order for", order)
			queue.enqueue(order)
			time.sleep(0.5)

	def serve_order(queue):
		time.sleep(1)
		while queue.size()!=0:
			order = queue.dequeue()
			print("This order is ready", order)
			time.sleep(2)

	queue = Queue()
	orders = ['pizza','samosa','pasta','biryani','burger']

	placing_thread = threading.Thread(target=place_order, args=(orders,))
	serving_thread = threading.Thread(target=serve_order, args=(queue,))

	placing_thread.start()
	serving_thread.start()

	placing_thread.join()
	serving_thread.join()

	



