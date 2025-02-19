class Node:
    def __init__(self, pid, burst_time):
        self.pid = pid
        self.burst_time = burst_time
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.tail = None

    def append(self, pid, burst_time):
        new_node = Node(pid, burst_time)
        if not self.tail:
            self.tail = new_node
            self.tail.next = self.tail
        else:
            new_node.next = self.tail.next
            self.tail.next = new_node
            self.tail = new_node

    def remove(self, node):
        if self.tail == node and self.tail.next == self.tail:
            self.tail = None
        else:
            prev = self.tail
            current = self.tail.next
            while current != node:
                prev = current
                current = current.next
            prev.next = current.next
            if self.tail == node:
                self.tail = prev

    def is_empty(self):
        return self.tail is None

def round_robin_scheduler(processes, quantum_time):
    cll = CircularLinkedList()
    for pid, burst_time in processes:
        cll.append(pid, burst_time)

    current_time = 0
    while not cll.is_empty():
        current = cll.tail.next
        start_time = current_time
        
        print(f"Time: {current_time}, Processing PID: {current.pid}")
        if current.burst_time <= quantum_time:
            current_time += current.burst_time
            print(f"Process {current.pid} completed.")
            cll.remove(current)
        else:
            current_time += quantum_time
            current.burst_time -= quantum_time
            print(f"Process {current.pid} now has {current.burst_time} units remaining.")
            cll.tail = current

    print(f"All processes completed. Total time taken: {current_time}")

# Example usage:
processes = [(1, 10), (2, 5), (3, 8)]
quantum_time = 4
round_robin_scheduler(processes, quantum_time)
