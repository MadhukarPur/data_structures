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