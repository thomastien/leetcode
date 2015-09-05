'''
push(x) -- Push element x to the back of queue.
pop() -- Removes the element from in front of queue.
peek() -- Get the front element.
empty() -- Return whether the queue is empty.

'''


class Queue(object):    
    def __init__(self):       
        self.stack = []

    def push(self, x):     
        self.stack += str(x)
        
    def pop(self):        
        if len(self.stack) > 0:
            self.stack.pop(0)

    def peek(self):      
        if len(self.stack) == 0:
            return None
        else:
            return int(self.stack[0])

    def empty(self):    
        if len(self.stack) ==0:
            return True
        else:
            return False 
