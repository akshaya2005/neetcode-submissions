class MinStack:

    def __init__(self):
        self.min = float('inf')
        self.stack = []

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append((val, float('inf')))
            self.min = val
        else:
            self.stack.append((val, self.min))
            if val < self.min:
                self.min = val
        

    def pop(self) -> None:
        if not self.stack:
            return
        pop, prevMin = self.stack.pop()
        if pop == self.min:  
            self.min = prevMin
        

    def top(self) -> int:
        top, _ = self.stack[-1]
        return top
    
        

    def getMin(self) -> int:
        return self.min
        
