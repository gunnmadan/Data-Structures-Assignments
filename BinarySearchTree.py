class BinarySearchTree:
    class Node: #represents a binary tree node
        def __init__(self, value, l=None, r=None):
            self.value = value
            self.left = l
            self.right = r

    def __init__(self):
        self.root = None

    def insert(self, value):
        self.root = self._insert(self.root, value)

    def _insert(self, node, value):
        if node is None:
            return self.Node(value)

        if value > node.value:
            node.right = self._insert(node.right, value)
        else:
            node.left = self._insert(node.left, value)

        return node

    def find(self, value):
        return self._find(self.root, value)

    def _find(self, node, value):
        if node is None:
            return False
        if node.value == value:
            return True
        if value > node.value:
            return self._find(node.right, value)
        return self._find(node.left, value)

    def delete(self, value):
        self.root = self._delete(self.root, value)

    def _delete(self, node, value): #find the node to be deleted
        if node is None:
            return node  # Base case: node not found

        if value < node.value:
            node.left = self._delete(node.left, value)  # Search in the left subtree
            return node
        elif value > node.value:
            node.right = self._delete(node.right, value)  # Search in the right subtree
            return node
        else:
            return self._delete_node(node)  # Node found, proceed to deletion

    def _delete_node(self, node):
        if node.left is None:
            return node.right
        if node.right is None:
            return node.left

        # Find the in-order successor (smallest value in the right subtree)
        node.value = self.in_order_successor(node.right).value
        # Delete the in-order successor
        node.right = self._delete(node.right, node.value)
        return node

    def in_order_successor(self, node):
        successor = node

        while successor.left is not None:
            successor = node.left

        return successor

    def height(self, node):
        if node is None:
            return -1
        return 1 + max(self.height(node.left), self.height(node.right))

    def get_nodes_at_distance(self, dist, node, nodes_list):
        if node is None:
            return
        if dist == 0:
            nodes_list.append(node.value)
        self.get_nodes_at_distance(dist - 1, node.left, nodes_list)
        self.get_nodes_at_distance(dist - 1, node.right, nodes_list)

    def traverse_level_order(self):
        result = []
        for dist in range(self.height(self.root) + 1):
            nodes_at_distance = []
            self.get_nodes_at_distance(dist, self.root, nodes_at_distance)  # Pass the list
            result.append(nodes_at_distance)
        return result

#Driver code:
bst = BinarySearchTree()

# Test insertions
values = [7, 3, 9, 1, 5, 8, 10]
print("Inserting values:", values)
for value in values:
    bst.insert(value)

# Test find()
find_values = [5, 2, 9]
print("\nFinding values:")
for value in find_values:
    found = bst.find(value)
    print(f"Value {value} found: {found}")

# Test level-order traversal
print("\nLevel-order traversal:")
level_order = bst.traverse_level_order()
print(level_order)

# Test delete
values_to_delete = [3, 7, 1]
print("\nDeleting values:", values_to_delete)
for value in values_to_delete:
    bst.delete(value)

# Level-order traversal after deletions
print("\nLevel-order traversal after deletions:")
level_order_after_deletion = bst.traverse_level_order()
print(level_order_after_deletion)

