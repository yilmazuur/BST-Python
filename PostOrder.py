"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.data (the value of the node)
"""
def postOrder(root):
    if root is None:
        return
    if root.left is not None:
        postOrder(root.left)
    if root.right is not None:
        postOrder(root.right)
    print(root.data, end=' ')