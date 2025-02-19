class ListNode:
    def __init__(self, value = 0, next = None):
        self.value = value
        self.next = next
    
def get_cycle_length(node):
    slow = node
    fast = node
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return calculate_length(slow)
            
        return 0
    
def calculate_length(meeting_point):
    current = meeting_point
    length = 0
    while True:
        current = current.next
        length += 1
        if current == meeting_point:
            break
    return length   
