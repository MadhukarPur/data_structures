'''
Doubly Linked Lists - A linked list where a node points to both its previous and next elements.

Applications of Doubly linked Lists:-
    Doubly linked lists find applications beyond text editors, including task scheduling, cache management, 
    and doubly ended queue implementations.


'''

class Node:
    def __init__(self, data):
        self.prev = None
        self.data = data
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    # traverse the linked list
    def traverse(self):
        # start at head
        current = self.head
        print("None", end = " <-> ")
        # loop until the node is None
        while current is not None:
            print(f"{current.data} <-> ", end="") 
            current = current.next
        print("None")
    
    # reverse traverse the linked list
    def reverse_traverse(self):
        # start at tail
        current = self.tail
        print("None", end = " <-> ")
        # loop until node is None
        while current is not None:
            print(f"{current.data} <-> ", end="") 
            current = current.prev
        print("None")
    
    # helper method to get the length of the list
    def length(self):
        length = 0
        current = self.head
        while current:
            length += 1
            current = current.next
        return length
        
    # insert at the end (append)
    def append_node(self, data):
        # initialize a new node
        new_node = Node(data)
        # update links
        new_node.prev = self.tail
        self.tail.next = new_node
        #  update tail
        self.tail = new_node

    # append to empty list
    def append_to_empty(self, data):
        new_node = Node(data)
        self.head = new_node
        self.tail = new_node
    
    # insert at beginning
    def insert_at_beginning(self, data):
        # create new node
        new_node = Node(data)
    
        # update pointers
        new_node.next = self.head
        self.head.prev = new_node
    
        # update head
        self.head = new_node
    
    # insert at position
    def insert_at_position(self, position, data):
        # create new node
        new_node = Node(data)
        # bring a pointer to desired position 
        current = self.head
        for i in range(position - 1):
            current = current.next
        
        # get a pointer to the next node
        next_node = current.next

        # update pointers
        current.next = new_node
        next_node.prev = new_node

        new_node.prev = current
        new_node.next = next_node
    
    # delete from beginning
    def delete_from_beginning(self):
        # get reference to the head node
        current = self.head
        # shift head
        self.head = self.head.next
        # update prev of head
        self.head.prev = None
        # update the next of current 
        current.next = None
    
    # delete a linked list with a single element
    def delete_single_element(self):
        self.head = None
        self.tail = None
    
    # delete from end
    def delete_from_end(self):
        # get reference to the tail node
        current = self.tail
        # shift tail
        self.tail = self.tail.prev
        # update next of tail
        self.tail.next = None
        # set the previous of current to None
        current.prev = None
    
    # delete from given position 
    def delete_from_position(self, position):
        # get reference to the nodes before
        # and after the given position 
        current = self.head
        prev_node = next_node = None
        for i in range(position-1):
            current = current.next
        prev_node = current.prev
        next_node = current.next
    
        # update pointers
        prev_node.next = next_node
        next_node.prev = prev_node
    
        # delete node
        current.next = None
        current.prev = None
    
    def insert_node(self, data, position = None):
        # check if the list is empty
        # and append to empty list
        if self.head is None:
            self.append_to_empty(data)
            return  # exit after handling this case
    
        # if position is None or not provided,
        # append the node to the end
        if position is None:
            self.append_node(data)
            return  # exit after handling this case
    
        # if position is 0, insert at the beginning
        if position == 0:
            self.insert_at_beginning(data)
            return  # exit after handling this case
    
        # for a valid position,
        # get the current length of the list
        length = self.length()
    
        # if position exceeds length,
        # append the node
        if position >= length:
            self.append_node(data)
            return  # exit after handling this case
    
        # if none of the above conditions are met
        # insert at the specified position
        self.insert_at_position(position, data)

    # universal delete method
    def delete_node(self, position=None):
        # check if the list is empty
        if self.head is None:
            print("The list is empty.")
            return
        
        # single element case
        if self.length() == 1:
            self.delete_single_element()
            return
    
        # first element case
        if position == 1:
            self.delete_from_beginning()
            return
        
        # last element case (or no position given)
        if position is None or position == self.length():
            self.delete_from_end()
            return
    
        # specific position case
        if 1 < position < self.length():
            self.delete_from_position(position)
            return
        else:
            print("Invalid position.")
            return
    
    def reverse(self):
        # no need to reverse in case of 0 or 1 nodes
        if self.length() < 2:
            return
        
        # start from head
        current = self.head
        while True:
            # swap previous and next node pointers
            current.prev, current.next = current.next, current.prev
            
            # move to the new previous node
            current = current.prev
            
            # repeat until you reach None
            if current == None:
                break
            
        # swap head and tail
        self.head, self.tail = self.tail, self.head

    # check if list is palindrome
    def is_palindrome(self):
        # palindrome doesn't apply for empty linked lists
        if not self.head:
            return False
        
        if self.length() < 2:
            return True
        
        # get reference to both head and tail
        start = self.head
        end = self.tail
    
        while start != end and start.prev != end:
            # return False if data don't match
            if start.data != end.data:
                return False
            # move forward from head
            # and backward from tail
            start = start.next
            end = end.prev
            # repeat until end is
            # no longer after start
            if(start == end or start == end.next):
                return True
            
linked_list = DoublyLinkedList()
list1 = [11, 22, 33, 44]
for i in list1:
    linked_list.insert_node(i)

print("Original Linked List:")
linked_list.traverse()

print()

print("Reversed Linked List:")
linked_list.reverse()
linked_list.traverse()