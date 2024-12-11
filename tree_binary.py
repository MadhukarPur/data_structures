'''
    What are Binary Trees?
        A binary tree is a tree that has, at most, two children.

        The properties of binary tree are:
            -- Every node has, at most, two children.
            -- Each child node is classified as either a left node or a right node.
            -- The left child always precedes the right child in the order of the nodes.
            -- n general, a tree with height h has, at most, (2 ^ (h+1) - 1) nodes
        
        A binary tree node will have three core information:
            -- The data value
            -- The location of the left child
            -- The location of the right child
'''

class BinaryTreeNode:
    def __init__(self,data) -> None:
        self.data = data
        self.left = None
        self.right = None

    def add_left_child(self,node):
        self.left = node
    
    def add_right_child(self,node):
        self.right = node

class BinaryTree:
    def __init__(self,root=None) -> None:
        self.root = root

    def print_all_paths(self):
        self.print_paths(self.root, [])

    def print_paths(self, current_node, path):
        # write your code here
        if current_node is None:
            return

        # append the current node to the path
        path.append(current_node.data)

        # if it's a leaf node, print the path
        if current_node.left is None and current_node.right is None:
            print(path)
        else:
            # otherwise, continue with the left and right children
            self.print_paths(current_node.left, path.copy())
            self.print_paths(current_node.right, path.copy())

Node_Root = BinaryTreeNode('Root')
Node_Left = BinaryTreeNode('Left')
Node_Right = BinaryTreeNode('Right')
Node_Root.add_left_child(Node_Left)
Node_Root.add_right_child(Node_Right)

tree = BinaryTree(Node_Root)
tree.print_all_paths()