class unlimited_stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return "Stack is empty!"
            
    
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return "Stack is empty!" 
            
        
    def is_empty(self):
        return len(self.items) == 0

stack = unlimited_stack()
(stack.push(1))
(stack.push(2))
(stack.push(3))
(stack.push(1))
print(stack.items)
print(stack.pop())
print(stack.peek())