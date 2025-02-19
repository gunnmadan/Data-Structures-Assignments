from collections import deque

#Definition for a binary tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left #left child
        self.right = right #right child

def recoverFromPreorder(traversal: str):
    '''
    Reconstructs a binary tree from a preorder traversal string with depth encoding.
    '''
    i, n = 0, len(traversal) #initialize pointer and string length
    stack = [] #stack to manage nodes at each depth during construction
    
    while i < n:
        #determine the depth of the current node by counting dashes
        depth = 0
        while i < n and traversal[i] == '-':
            depth += 1
            i += 1
        #Extract the value of the node
        value = 0
        while i < n and traversal[i].isdigit():
            value = value * 10 + int(traversal[i])
            i += 1
        # Create a new TreeNode
        node = TreeNode(value)
        # Adjust stack to maintain the correct parent-child relationship
        while len(stack) > depth:
            stack.pop()
        if stack: #attach the new node to its parent
            parent = stack[-1]
            if not parent.left: #assign as left child if vacant
                parent.left = node
            else: #otherwise, assign as right child
                parent.right = node
        stack.append(node)
    
    # The root of the tree is the first node in the stack
    root = stack[0]
    
    # Perform level order traversal
    return levelOrderTraversal(root)

def levelOrderTraversal(root):
    """
    Performs level order traversal (BFS) and returns node values level by level.
    """
    if not root:
        return [] #return empty list if tree is empty
    result = []
    queue = deque([root]) #Queue for BFS
    while queue:
        #Traverse all nodes at the current level
        level = []
        for _ in range(len(queue)):
            node = queue.popleft()
            if node:
                level.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
            else:
                level.append(None)
        result.extend(level)
    # Remove trailing None values
    while result and result[-1] is None:
        result.pop()
    return result

# Example usage
traversal1 = "1-2--3--4-5--6--7"
traversal2 = "1-2--3---4-5--6---7"

print(recoverFromPreorder(traversal1))  # Output: [1, 2, 5, 3, 4, 6, 7]
print(recoverFromPreorder(traversal2))  # Output: [1, 2, 5, 3, None, 6, None, 4, None, 7]
