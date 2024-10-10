'''
Linked List - A linked list is a linear data structure that includes a series of connected elements. 
            Each element of a linked list is called a node.
            A node stores data and the address of the next node.
                data - value of a node
                next - address of the next node
                
Time Complexity: O(n)

Operations in a linked list:
    -- Inserting into a linked list
    -- Deleting from a linked list
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def create_linked_list(self):
        node1 = Node(80)
        self.head = node1

        node2 = Node(9)
        node1.next = node2

        node3 = Node(14)
        node2.next = node3

    # method to append a node at the end
    def append_node(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    # method to insert a node at the beginning
    def insert_node_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # method to insert a node at a specific position
    def insert_node_at_position(self, data, position):
        new_node = Node(data)
        current = self.head

        for i in range(1, position - 1):
            current = current.next
        
        new_node.next = current.next
        current.next = new_node

    # universal insert method
    def insert_node(self, data, position=None):
        if position is None:
            self.append_node(data)
            return

        if position <= 0 or position > self.get_length() + 1:
            print("Invalid position")
            return

        if position == 1:
            self.insert_node_at_beginning(data)
        elif position == self.get_length() + 1:
            self.append_node(data)
        else:
            self.insert_node_at_position(data, position)

    # helper method to get the length of the linked list
    def get_length(self):
        current = self.head
        length = 0
        while current:
            length += 1
            current = current.next
        return length

    # traverse the list
    def display(self):
        current = self.head
        while current:
            print(f"{current.data}", end="->")
            current = current.next
        print(None)

    # method to delete the first node
    def delete_node(self):
        # Time Complexity : O(1)
        if self.head:
            self.head = self.head.next

    # method to delete a node at the given position
    def delete_node(self, position):
        # Time Complexity: O(n)
        # Check if the position is valid
        if position <= 0 or position > self.get_length():
            print("Invalid position")
            return

        # if linked list is empty
        if not self.head:
            return

        # condition to delete node at the first position
        if position == 1:
            self.head = self.head.next
            return

        current = self.head

        # Traverse the list to find the node before the one to be deleted
        for i in range(1, position - 1):
            # condition to handle if position
            # is greater than number of nodes
            if not current.next:
                return
            current = current.next        

        # current.next is the node to be deleted
        # current.next.next is the node after the node to be deleted
        if current.next:
            current.next = current.next.next

    def concatenate(self, list2):
        # handle if the first linked list is empty
        if not self.head:
            self.head = list2.head
            return
        
        current = self.head 

        # traverse the linked list
        while current.next:
            current = current.next
         
        # link the last node of list1 to
        # the first node of list2 
        current.next = list2.head

    def reverse_linked_list(self):
        # write your code here
        prev_node = None
        current = self.head
        next_node = current.next

        while True:
            current.next = prev_node

            prev_node = current
            current = next_node
            next_node = next_node.next

            if next_node == None:
                current.next = prev_node
                break

        self.head = current

    def find_smallest(self):
        # write your code here
        current = self.head
        smallest = current.data
        while current.next != None:
            current = current.next
            if smallest > current.data:
                smallest = current.data

        return smallest
    
    # method to return the middle element 
    def find_middle_element(self):
        # write your code here 
        slow,fast = self.head,self.head
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next
            
            
        return slow.data
# example usage
linked_list = LinkedList()
linked_list.create_linked_list()

print("Original Linked List:")
linked_list.display()
print()

# insert at the beginning
linked_list.insert_node(1, 1)
print("After inserting 1 at position 1:")
linked_list.display()
print()

# insert without position (end)
linked_list.insert_node(15)
print("After inserting 15 without position:")
linked_list.display()
print()

# insert at a negative position
linked_list.insert_node(100, -1)
print("After inserting 100 at position -1:")
linked_list.display()
print()

# insert at a position beyond the list's length
linked_list.insert_node(50, 100)
print("After inserting 50 at position 100:")
linked_list.display()
print()

# insert at a valid position
linked_list.insert_node(55, 3)
print("After inserting 55 at position 3:")
linked_list.display()
print() 

# Practise questions on a linked list
'''
Find the largest number in a linked list.
Check if the linked list is sorted.
Remove duplicate nodes from a sorted linked list.
Reverse a linked list.
Concatenate two linked lists.
Practice: Find the smallest value in a linked list.
Practice: Find the middle node of a linked list.
'''

#