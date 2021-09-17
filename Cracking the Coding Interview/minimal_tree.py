# Question 4.2

# TODO: implement without additional data structure

# Input: sorted array
# Output: binary search tree with minimal height (this ends up just being the root node, no extra data structure needed)

class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.val = value

def min_tree(array):
    if len(array) < 1: return # TODO: could just be if not array?

    mid = len(array) // 2
    node = Node(array[mid])
    
    node.left = min_tree(array[:mid])
    node.right = min_tree(array[mid+1:])

    return node

# functions for testing code
def in_order_traverse(root):
    result = []
    stack = []

    current_node = root
    while current_node != None or len(stack) != 0: #TODO: make more pythonic
        while current_node != None:
            stack.append(current_node)
            current_node = current_node.left

        current_node = stack.pop()
        result.append(current_node.val)
        current_node = current_node.right

    return result

def height(bst):
    if bst == None:
        return 0
    else:
        return 1 + max(height(bst.left), height(bst.right))


test = [[1,2,3,4,5,6,7,8,9,10]]
expected_height = [4]

for i in range(len(test)):
    bst = min_tree(test[i])
    inorder = in_order_traverse(bst)
    actual_height = height(bst)
    assert inorder == test[i], f"Test {i}: expected: {test[i]}, recieved: {inorder}"
    assert actual_height == expected_height[i], f"Test {i}: expected: {expected_height[i]}, recieved: {actual_height}"