#Problem1
from heapq import heapify


def next_greater_element(arr):
    stack = []
    result = [-1] * len(arr)

    for i in range(len(arr) -1, -1, -1):
        while stack and stack[-1] <= arr[i]:
            stack.pop()
        if stack:
            result[i] = stack[-1]
        stack.append(arr[i])

    return result

#example usuage:
arr = [2, 1, 4, 3]
print(next_greater_element(arr))

#Problem 2
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def insert_into_circular_list(head, invertVal):
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

#Example usuage:
# Create the circular linked list [3, 4, 1]
head = Node(3)
node2 = Node(4)
node3 = Node(1)
head.next = node2
node2.next = node3
node3.next = head

new_head = insert_into_circular_list(head, 2)


    
