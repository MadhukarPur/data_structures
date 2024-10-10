'''
Circular Linked lists - Linked lists where the last node points back to the head node. This kind of linked list is called 
                a circular linked list.
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class CircularLinkedList:
    def __init__(self):
        self.head = None

    # helper to get length 
    def length(self):
        if not self.head:
            return 0
        current = self.head
        count = 1
        while current.next != self.head:
            current = current.next
            count += 1
        return count
    
    # helper to traverse the list 
    # and display the elements
    def display(self):
        nodes = []
        if self.head is None:
            return "Empty Linked List"
        current = self.head
        while current.next is not self.head:
            nodes.append(str(current.data))
            current = current.next
        nodes.append(str(current.data))
        return " -> ".join(nodes) + f" -> {self.head.data} "
    
    # helper to append into a empty linked list
    def append_into_empty(self, data):
        new_node = Node(data)
        self.head = new_node
        new_node.next = self.head
    
    # helper to append node into a non-empty linked list
    def append_node(self, data):
        new_node = Node(data)
        current = self.head
        while current.next != self.head:
            current = current.next
        current.next = new_node
        new_node.next = self.head
    
    # helper to insert node at the beginning
    def insert_at_beginning(self, data):
        new_node = Node(data)
        current = self.head
        while current.next != self.head:
            current = current.next
        current.next = new_node
        new_node.next = self.head
        self.head = new_node
    
    # helper to insert node at a position
    # except position = 1 ( beginning)
    def insert_at_position(self, data, position):
        new_node = Node(data)
        current = self.head
        for i in range(1, position - 1):
            current = current.next
        new_node.next = current.next
        current.next = new_node

    # universal method to insert node
    def insert_node(self, data, position=None):
        if not self.head:
            self.append_into_empty(data)
        elif not position or position == self.length() + 1:
            self.append_node(data)
        elif position == 1:
            self.insert_at_beginning(data)
        else:
            self.insert_at_position(data, position)
    

    # helper to delete from beginning
    def delete_from_beginning(self):
        # get a reference to head
        temp = self.head
        current = self.head
        # get a reference to the last node
        while current.next is not self.head:
            current = current.next
        # shift head to second node    
        self.head = self.head.next
        # adjust the next pointer of the last node to the new head
        current.next = self.head

    # helper to delete the only node of the linked list
    def delete_only_node(self):
        temp = self.head
        self.head = None
    
    # delete at any given position
    def delete_at_position(self, position):
        # take two pointers
        current = self.head
        prev_node = None
        # move pointers until we reach our desired node
        for i in range(1, position):
            prev_node = current
            current = current.next
        # point the previous node to the current.next node
        prev_node.next = current.next
    
    def delete_nodes(self, position):
        # check if the list is empty
        if self.head is None:
            return "Error: The list is empty."

        # if position is 1, check if it's the only node
        if position == 1:
            if self.head.next == self.head:  # Only one node in the list
                self.delete_only_node()
            else:
                self.delete_from_beginning()
        else:
            # for positions other than 1, use delete_at_position
            # first, ensure the position is not out of bounds
            temp = self.head
            count = 1
            while temp.next != self.head:
                count += 1
                temp = temp.next
            
            if position > count:
                return "Error: Position is out of bounds."

            self.delete_at_position(position)


linked_list = CircularLinkedList()

# Example usage 

# create a new circular linked list
linked_list = CircularLinkedList()

# create the linked list with initial nodes
linked_list.insert_node(80)
linked_list.insert_node(9)
linked_list.insert_node(14)

# display the initial list
print("Initial list:")
print(linked_list.display())  
print()

# insert a node at the beginning
linked_list.insert_node(5, 1)
print("After inserting 5 at the beginning:")
print(linked_list.display())
print()

# insert a node at the end
linked_list.insert_node(25)
print("After appending 25 at the end:")
print(linked_list.display())
print()  

# insert a node at position 3
linked_list.insert_node(55, 3)
print("After inserting 55 at position 3:")
print(linked_list.display())
print()

# delete the first node
linked_list.delete_nodes(1)
print("After deleting the first node:")
print(linked_list.display())
print() 

# delete the node at position 2
linked_list.delete_nodes(2)
print("After deleting the node at position 2:")
print(linked_list.display())
print()

# delete the last node
linked_list.delete_nodes(linked_list.length())
print("After deleting the last node:")
print(linked_list.display())