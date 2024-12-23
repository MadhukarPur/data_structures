'''
Doble Ended Queue: Deque is a double ended queue, and we can use any end to insert and delete elements.
            The deque does not necessarily follow the First-In-First-Out principle.
'''

class Deque:
    def __init__(self):
        # initialize an empty deque
        self.deque = []

    # write method to add element from the rear end
    def add_rear(self,item):
        self.deque.append(item)

    # write method to add element from the front end
    def add_front(self,item):
        self.deque.insert(0,item)

    # write method to delete  element from the front end
    def remove_front(self):
        self.deque.pop(0)

    # write method to remove element from the rear end
    def remove_rear(self):
        self.deque.pop()
        
    # method to print the queue
    def print_queue(self):
        print(self.deque)

d = Deque()

# take number inputs
input_str = input()

# split the input and convert it to integers 
number1, number2, number3, number4 = [int(val) for val in input_str.split()]

# insert number1 and number2 from the rear
d.add_rear(number1)
d.add_rear(number2)
d.print_queue()

# insert number3 and number4 from the front
d.add_front(number3)
d.add_front(number4)
d.print_queue()

# remove one element from the rear
d.remove_rear()
d.print_queue()

# remove one element from the front
d.remove_front()
d.print_queue()