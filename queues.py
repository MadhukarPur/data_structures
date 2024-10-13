'''
    Linear Queue - The queue is a first-in-first-out (FIFO) data structure. A queue data structure is similar to a queue in real life.

    Time Complexity: O(1)

    Drawbacks of Linear Queue:
        In a linear queue we:
            -- enqueued an element using append()
            -- dequeued an element pop(0)
        
        While it is easy to implement, it is inefficient.

        In linear queues, once an element is dequeued, its space is not utilized again. Over time, this leads to a waste of memory.
'''

class Queue:
    def __init__(self) -> None:
        self.queue_list = []

    def enqueue(self,data):
        self.queue_list.append(data)

    def dequeue(self):
        return self.queue_list.pop(0)
    
    def print_queue(self):
        print(self.queue_list)
    
    # return True if queue is empty. return False if queue is not empty
    def is_empty(self):
        return len(self.queue) == 0
    
    # function to peek the queue
    def peek(self):
        if not self.is_empty():
            return self.queue[0]


q_obj = Queue()
q_obj.enqueue(10)
q_obj.enqueue(20)
q_obj.enqueue(30)
q_obj.enqueue(40)
q_obj.print_queue()
q_obj.dequeue()
q_obj.print_queue()
q_obj.dequeue()
q_obj.print_queue()

        