from queue import Queue

class StackInAQueue:
    def __init__(self):
        self.q1 = Queue()
        self.q2 = Queue()

    def push(self, item):
        self.q2.put(item)
        while not self.q1.empty():
            self.q2.put(self.q1.get())
        self.q1, self.q2 = self.q2, self.q1

    def pop(self):
        if self.q1.empty():
            return None
        return self.q1.get()
    
    def __len__(self):
        return self.q1.qsize()
    
    def top(self):
        if self.q1.empty():
            return None
        return self.q1.queue[0]
    
    def push_k_items(self, k, items):
        for item in items:
            self.q2.put(item)
        while not self.q1.empty():
            self.q2.put(self.q1.get())
        self.q1, self.q2 = self.q2, self.q1
    
#Example Usuage
stack = StackInAQueue()
stack.push(1)
stack.push(2)
stack.push(3)
print(stack.top())
stack.push_k_items(2, [4, 5])
print(stack.top())
print(stack.pop())
print(stack.top())
print(len(stack))

