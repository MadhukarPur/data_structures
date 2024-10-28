#  Preorder Traversal
'''
    Preorder Traversal:
        Preorder traversal explores the tree in a root-left-right manner.
        
        Two things to remember in preorder traversal:
            -- Traversal takes from left to right.
            -- If the left child has descendants, you'll explore the left subtree fully before checking out the right one.

    Applications of Preorder Traversal:

        Preorder traversal is useful for tasks requiring parent node action before processing the children. Therefore, it's used in:

        1. Cloning a Tree
            Preorder traversal is the go-to method for cloning a tree. When we print a node right after visiting it, we get an instant copy of the given tree.
            The primary purpose of cloning a tree is to help in backup systems and security.

        2. Serialization
            Trees can be serialized (converted into a string) and deserialized (converted back to a tree) using preorder traversal, allowing them to be stored in 
            databases or sent across networks.
            It allows us to recreate the same tree structure at a later point in time or in a different computing environment.
'''
#  Postorder Traversal
'''
    Postorder Traversal:
        Postorder traversal explores the tree in a left-right-root manner.
        Here, we fully explore each child subtree before visiting the root node.

    Applications of Postorder Traversal:
        Postorder traversal is ideal for problems where processing a node relies on the results from its children. 
        While its applications are vast, here are some common use cases:

        1. Tree Deletion
            Postorder traversal is often used for deleting all nodes in a tree. It ensures that child nodes are deleted before their parents, minimizing the 
            risk of memory leaks. This is especially useful in languages without automatic garbage collection.

        2. Dynamic Programming
            Dynamic Programming is a powerful technique for solving complex problems by breaking them into smaller subproblems.
            Postorder traversal is commonly used in tree-based dynamic programming, as it allows you to solve child subproblems before tackling the parent node.
'''
# Breadth-First Tree Traversal
'''
    Breadth-First Tree Traversal (Level Order Traversal):
        Level order traversal, also known as breadth-first search, visits nodes in a level-by-level manner.
        For any general tree, we start from the root, visit all nodes at the current level, and then move to the next level.

    Application of Breadth-First Traversal:
        Breadth-first traversal is used in scenarios when we need to process all of the outcomes for a current node before processing the outcome of the branch nodes.
        The most common use of this traversal is in Game Trees used by the computer software to play games against the user.
'''
from collections import deque

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []

    def add_child(self, child):
        self.children.append(child)

class Tree:
    def __init__(self, root=None):
        self.root = root
 
    def preorder_traversal(self, node, traversal=[]):
        if not node:
            return traversal
        
        traversal.append(node.data)
        for child in node.children:
            self.preorder_traversal(child, traversal)
        
        return traversal
        
    def postorder_traversal(self, node, traversal=[]):
        if not node:
            return traversal
        for child in node.children:  
            self.postorder_traversal(child, traversal)
        traversal.append(node.data)
        return traversal

    def calculate_disk_space(self, node):
        # write your code here
        if not node:
            return 0

        total_size = node.size
        
        for child in node.children:
            total_size += self.calculate_disk_space(child)
        
        return total_size
           
    def breadth_first_traversal(self):
        if not self.root:
            return []

        queue = deque()
        queue.append(self.root)
        
        traversal = [] 

        while queue:
            current_node = queue.popleft()
            traversal.append(current_node.data)  
    
            for child in current_node.children:
                queue.append(child)
    
        return traversal  

A = TreeNode('A')
B = TreeNode('B')
C = TreeNode('C')
D = TreeNode('D')
E = TreeNode('E')
F = TreeNode('F')
G = TreeNode('G')

A.add_child(B)
A.add_child(C)
A.add_child(D)
B.add_child(E)
B.add_child(F)
E.add_child(G)

general_tree = Tree(A)

print(f'Preorder Traversal: {general_tree.preorder_traversal(general_tree.root)}')
print(f'Postorder Traversal: {general_tree.postorder_traversal(general_tree.root)}')
print(f'Breadth First Traversal: {general_tree.breadth_first_traversal()}')