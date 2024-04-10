class MinStack:

    def __init__(self):
        self.stack = []
        
    def push(self, val: int) -> None:
        self.stack.append(val)
        
    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        if not self.stack:
            return 0
        return self.stack[-1]
        

    def getMin(self) -> int:
        curr = 0 
        for i in self.stack:
            curr = min(i,curr)
        return curr
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()