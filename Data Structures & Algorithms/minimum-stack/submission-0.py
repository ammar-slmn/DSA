class MinStack:

    def __init__(self):
        self.stack = []
        

    def push(self, val: int) -> None:
        print("val to be pushed: ", val) 
        self.stack.append(val) 
        
    def pop(self) -> None:
        print("this is the stack, an element will be popped: ", self.stack)
        self.stack.pop()
        print("this is the stack, an element is be popped: ", self.stack)

    def top(self) -> int:
        print("this is the top element of the stack: ", self.stack[-1])
        return self.stack[-1]
        
    def getMin(self) -> int:
        tmp = [] 
        smallest = self.stack[-1]

        while len(self.stack): 
            smallest = min(smallest, self.stack[-1]) 
            tmp.append(self.stack.pop()) 
        
        while len(tmp): 
            self.stack.append(tmp.pop())


        print("this is the smallest element: ", smallest)
        return smallest

