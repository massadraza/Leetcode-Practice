class MinStack:
    """
    def __init__(self):
        self.items = []
        self.min = float("infinity")
        self.dq = collections.deque()

    def push(self, val: int) -> None:
        self.items.append(val)
        if val <= self.min:
            self.min = val
            self.dq.append(val)
        else:
            self.dq.appendleft(val)
        
    def pop(self) -> None:
        value = self.items.pop()
        if value == self.min:
            self.dq.pop()
            if self.dq:
                self.min = self.dq[-1]
            else:
                self.min = float("infinity")
        else:
            self.dq.remove(value)
        
    def top(self) -> int:
        return self.items[-1]

    def getMin(self) -> int:
        if self.min == float("infinity"):
            return None

        if self.dq:
            return self.min
        else:
            return None
    """    

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(val)
        
    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()
        
    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
      
        

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()