"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.data (the value of the node)
"""


def height(root):
    if root is None:
        return -1  # -1 because of edge count in max depth, return 0 if challenge asks about node countt
    else:
        return 1 + max(height(root.left), height(root.right))
