class Node():
    def __init__(self, e):
        self.left = None
        self.right = None
        self.val = e

def Binary(root, node):
    if root is None:
        root = node
    else:
        if root.val > node.val:
            if root.left is None:
                root.left = node
            else:
                Binary(root.left, node)
        else:
            if root.right is None:
                root.right = node
            else:
                Binary(root.right, node)
def pre_order(root):
    if not root:
        return
    print(root.val)
    pre_order(root.left)
    pre_order(root.right)

root = Node(1)
Binary(root, Node(2))
Binary(root, Node(3))
Binary(root, Node(5))
Binary(root, Node(4))
'''Binary(root, Node(18))
Binary(root, Node(29))'''

print("Pre Order: ")
print(pre_order(root))
