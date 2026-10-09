class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []
        self.min = float('inf')

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.stack[-1] < self.min:
            self.minStack.append(self.stack[-1])
            self.min = self.minStack[-1]
        else:
            self.minStack.append(self.min)
        
        

    def pop(self) -> None:
        del self.stack[-1]
        del self.minStack[-1]
        if len(self.minStack)>0:
            self.min = self.minStack[-1]
        else:
            self.min = float('inf')
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minStack[-1]


        
