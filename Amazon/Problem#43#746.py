"""
Implement a stack that has the following methods:
    push(val), which pushes an element onto the stack
    pop(), which pops off and returns the topmost element of the stack. If there are no elements in the stack, 
           then it should throw an error or return null.
    max(), which returns the maximum value in the stack currently. If there are no elements in the stack, 
           then it should throw an error or return null.
Each method should run in constant time.
"""
class maxStack:
    def __init__(self):
        self.stack = []
        self.maxS = []
    
    def push(self, data):
        self.stack.append(data)
        if not self.maxS or self.maxS[-1] <= data:
            self.maxS.append(data)

    def pop(self):
        if not self.stack:
            return None
        popData = self.stack.pop()
        if self.maxS[-1] == popData:
            self.maxS.pop()
        return popData
    
    def max(self):
        if not self.maxS:
            return None
        return self.maxS[-1]
