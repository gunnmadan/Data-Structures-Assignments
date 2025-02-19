class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def insert_into_circular_list(head, insertVal):
    new_node = Node(insertVal)
    if not head:
        new_node.next = new_node
        return new_node

    prev, curr = head, head.next
    to_insert = False

    while True:
        if prev.value <= insertVal <= curr.value:
            to_insert = True
        elif prev.value > curr.value:
            if insertVal >= prev.value or insertVal <= curr.value:
                to_insert = True

        if to_insert:
            prev.next = new_node
            new_node.next = curr
            return head

        prev, curr = curr, curr.next
        if prev == head:
            break

    prev.next = new_node
    new_node.next = curr
    return head

def print_list(head):
    if not head:
        print("List is empty")
        return
    
    print_values = []
    current = head
    while True:
        print_values.append(current.value)
        current = current.next
        if current == head:
            break

    print(" -> ".join(map(str, print_values)))

# Create the circular linked list [3, 4, 1]
head = Node(3)
node2 = Node(4)
node3 = Node(1)
head.next = node2
node2.next = node3
node3.next = head

# Insert 2
new_head = insert_into_circular_list(head, 2)

# Print the list
print_list(new_head)
