"""
    class Node:
       int data
       Node left
       Node right
"""

def leftView(node):
{
    if node is None:
        return
    leftView(node.left)
    print(node.data, end=" ")
}

def rightView(node):
{
    if node is None:
        return
    print(node.data, end=" ")
    rightView(node.right)
}

def top_view(root):
{
    if root is None:
        return
     
    leftView(root.left)
    print(root.data, end=" ")
    rightView(root.right)
}