class Node: 
    def __init__(self, value, left =None, right= None):
        self.value = value
        self.left = left
        self.right = right

#construct the parse tree for ((7+3)*(5-2))
root = Node('*')
root.left = Node('+')
root.right = Node('-')
root.left.left = Node(7)
root.left.right = Node(3)
root.right.left = Node(5)
root.right.right = Node(2)

def evaluate(node):
    if node.left is None and node.right is None:
        return node.value
    
    left_val = evaluate(node.left)
    right_val = evaluate(node.right)

    if node.value == '+':
        return left_val + right_val
    elif node.value == '-':
        return left_val - right_val
    elif node.value == '*':
        return left_val * right_val
    elif node.value == '/':
        return left_val / right_val
    else:
        raise ValueError('Invalid Operator')
    
print(evaluate(root)) #Should print 30.0