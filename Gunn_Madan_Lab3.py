class TwoStacks: 
    def __init__(self, n):
        #Create a list of size n and initialize pointers for both stacks
        self.n = n
        self.arr = [None] * n
        self.left_top = -1 #Left Stack pointer
        self.tight_top = n #Right stack pointer

    def push_left(self, item):
        #Check if there is space for the left stack
        if self.left_top + 1 < self.right_top:
            self.left_top += 1
            self.arr[self.left_top] = item

        else: 
            print("Stack Overflow: Left stack if full.")

    def push_right(self, item):
        if self.top_right > self.top_left + 1:
            self.top_right -= 1
            self.arr[self.top_right] = item

        else: 
            print("Stack Overflow")

    def pop_left(self):
        if self.top_left >= 0:
            popped_item = self.arr[self.top_left]
            self.arr[self.top_left] = None
            self.top_left -=1
            return popped_item
        
        else: 
            print ("Stack Underflow")
            return None
        
    def pop_right(self):
        if self.top_right < self.size:
            popped_item = self.arr[self.top_right]
            self.arr[self.top_right] = None
            self.top_right += 1
            return popped_item 
        else:
            print("Stack Underflow")
            return None
        
    def len_left(self):
        return self.top_left + 1
    
    def len_right(self):
        return self.size - self.top_right