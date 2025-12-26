class MinStack:

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
        

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()