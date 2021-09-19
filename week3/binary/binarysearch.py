# Binary tree node
class Node(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Convert sorted array to a balanced BST.
# Inputting an array of numbers, and receiving a root node of a balanced BST
def arrayToBST(numbers):
    
    if not numbers:
        return None
    
    # finding the middle
    mid_val = len(numbers)//2

    node = Node(numbers[mid_val])
    
    # left subtree has all values less than numbers[mid_val]
    node.left = arrayToBST(numbers[:mid_val])

    # right subtree has all values mroe than numbers[mid_val]
    node.right = arrayToBST(numbers[mid_val+1:])

    # return the node
    return node

# Traversal for printing of the BST
def preOrder(node): 
    if not node: 
        return      
    print(node.val)
    preOrder(node.left) 
    preOrder(node.right)   
    
result = arrayToBST([1, 2, 3, 4, 5, 6, 7])
preOrder(result)