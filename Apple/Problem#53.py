"""
Implement a queue using two stacks. Recall that a queue is a FIFO (first-in, first-out) data structure with the 
following methods: enqueue, which inserts an element into the queue, and dequeue, which removes it.
"""
class MyQueue:

    def __init__(self):
        self.s1 = []
        self.s2 = []
        
    def enqueue(self, x):
        self.s1.append(x)
        
    def dequeue(self):
        if self.empty():
            return None
        self.shiftStack()
        return self.s2.pop()

    def shiftStack(self):
        if len(self.s2) == 0:
            while self.s1:
                self.s2.append(self.s1.pop())
                
    def empty(self):
        return True if (len(self.s1)+len(self.s2)) <= 0 else False