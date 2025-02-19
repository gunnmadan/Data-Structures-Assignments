class CustomStack:
    def __init__(self):
        self._data = []

    def push(self, item):
        self._data.append(item)

    def is_empty(self):
        return len(self._data) == 0

    def pop(self):
        if self.is_empty():
            return None
        return self._data.pop()

    def top(self):
        if self.is_empty():
            return None
        return self._data[-1]

    def __len__(self):
        return len(self._data)

stack = CustomStack()
stack.push(1)
stack.push(2)
stack.push(3)

remove_all(stack):
print (len(stack))
def remove_all(stack):
    #
    
def reverse_list(lst):
    #

