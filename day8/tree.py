# Tree:
# Collection of nodes connected by edges.

# Node:
# Element that stores data.

# Root:
# Topmost node of the tree.

# Parent:
# Node having child nodes.

# Child:
# Node connected below a parent.

# Leaf Node:
# Node having no children.

# Edge:
# Connection between two nodes.

# Height:
# Longest path from root to leaf.

# Depth:
# Distance of a node from root.


        #       A          ← Root
        #     /   \
        #    B     C       ← Children
        #   / \
        #  D   E           ← Leaf Nodes


# -------------------- Binary Tree---------------------------------------

# A Binary Tree is a tree where each node can have maximum 2 children.

# Children are called:

# Left Child
# Right Child

# Example:

#              10
#            /    \
#           20     30
#          / \
#         40  50

#------------------ Binary Search Tree (BST)-----------------------------------------

# A Binary Search Tree is a special type of Binary Tree where data follows a rule:

# Left Child < Root < Right Child

# Example:

#               50
#             /    \
#           30      70
#          /  \    /  \
#        20   40 60   80

# Rules:

# Left side contains smaller values.
# Right side contains greater values.


class Node:
    def __init__(self, data):
        self.left = None
        self.data = data
        self.right = None


class Tree:
    def __init__(self):
        self.root = None

    def createNode(self, data):
        newNode = Node(data)
        self.insert(newNode)

    def insert(self, newNode):
        if self.root is None:
            self.root = newNode
            return

        queue = [self.root]

        while queue:
            temp = queue.pop(0)

            if temp.left is None:
                temp.left = newNode
                return
            else:
                queue.append(temp.left)

            if temp.right is None:
                temp.right = newNode
                return
            else:
                queue.append(temp.right)

    def display(self):
        self.inorder(self.root)

    def inorder(self, root):
        if root is not None:
            self.inorder(root.left)
            print(root.data, end=" ")
            self.inorder(root.right)


# Driver Code
t = Tree()

t.createNode(10)
t.createNode(20)
t.createNode(30)
t.createNode(40)
t.createNode(50)

print("Inorder Traversal:")
t.display()