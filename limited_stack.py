class limited_stack:
    def __init__(self, limit):
        self.items = []
        self.limit = limit

    def push(self, item):
        if len(self.items) < self.limit:
            return self.items.append(item)
        else:
            return "Stack is overflow!"
        
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return "Stack is underflow!"
            
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return "Stack is empty!" 
        
    def is_empty(self):
        return len(self.items) == 0

stack = limited_stack(3)
print(stack.push(1))
print(stack.push(2))
print(stack.push(3))
print(stack.push(4))
print(stack.items)
print(stack.pop())
print(stack.peek())