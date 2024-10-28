'''
    Limitations of Linear Data Structures:
        --  The primary limitation of linear data structures is that they cannot naturally represent hierarchical or branching relationships, as each 
            element is limited to exactly one predecessor and one successor.
        --  They do not provide optimal solution when the elements are characterized by a one-to-many relationship.
'''

# Introduction to Trees
'''
    Introduction to Trees:

        A tree is a non-linear data structure that represents relationships and connections among various elements, facilitating easy navigation and search.
        The primary purpose of a tree is efficient data organization.

        In a tree, nodes are the individual elements, and edges connect these nodes.

    Advantages fo using Tree:
        Trees clearly show the structure and hierarchy of directories and files, including parent-child relationships.


    Depth of a Tree:
        -- The depth of a node in a tree refers to the path length from the root node to that particular node.
        -- Depth is measured using the number of edges required to reach a particular node from the root node.
        -- The depth of the root node is zero since it does not have any ancestors.

    Height of a Tree:
        -- The height of a node in a tree refers to the length of the longest path from that node to a descendant leaf node.
        -- Height is measured using the number of edges encountered when moving from the node to the deepest child node.
        -- The height of a leaf node is zero since it has no children.

    Degree of a Node:
        -- The degree of a node is the number of children that the node has.
        -- The degree of a tree is the maximum degree of any node in the tree.

    Level of a Tree:
        In a tree data structure, the nodes are arranged at different levels.
            -- The root node is at Level 0.
            -- The nodes directly connected to the root are called Level 1 nodes.
            -- Each Level 1 node can have its own set of child nodes, which become Level 2 nodes.

    Subtree:
        A subtree is a portion of a tree that is derived from a specific node. This node is known as the subtree root.
'''

# create a class to handle the creation of node and addition of child nodes
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []

    def add_child(self, child):
        self.children.append(child)

# class to handle the creation of trees and operations performed in it
class Tree:
    def __init__(self, root=None):
        self.root = root
    
    def get_nodes_at_depth(self, node, depth):
        if not node:
            return []
        
        if depth == 0:
            return [node.data]
        
        if node and depth > 0:
            result = []
            for child in node.children:
                result += self.get_nodes_at_depth(child, depth - 1)
            return result

# creating our root node
root = TreeNode("Book")

# creating the children of root
child1 = TreeNode(1)
child2 = TreeNode(2)
child3 = TreeNode(3)

# creating our leaf nodes
child1_1 = TreeNode(1.1)
child1_2 = TreeNode(1.2)
child1_3 = TreeNode(1.3)
child1_4 = TreeNode(1.4)
child2_1 = TreeNode(2.1)
child3_1 = TreeNode(3.1)
child3_2 = TreeNode(3.2)
child3_3 = TreeNode(3.3)

# describing relationships between the nodes

# add children to the root node
root.add_child(child1)
root.add_child(child2)
root.add_child(child3)

# add children to child1
child1.add_child(child1_1)
child1.add_child(child1_2)
child1.add_child(child1_3)
child1.add_child(child1_4)

# add children to child2
child2.add_child(child2_1)

# add children to child3
child3.add_child(child3_1)
child3.add_child(child3_2)
child3.add_child(child3_3)

# creating our tree
tree = Tree(root)
for i in range(0,3):
    print(f"nodes at depth {i}: {tree.get_nodes_at_depth(root, i)}")