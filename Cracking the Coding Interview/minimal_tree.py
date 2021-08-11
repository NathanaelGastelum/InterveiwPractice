# Question 4.2

# Input: sorted array
# Output: binary search tree with minimal height (this ends up just being the root node, no extra data structure needed)

class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.val = value

def min_tree(array):
    if len(array) < 1: return

    mid = len(array) // 2
    node = Node(array[mid])
    
    node.left = min_tree(array[:mid])
    node.right = min_tree(array[mid+1:])

    return node

# TODO: test code