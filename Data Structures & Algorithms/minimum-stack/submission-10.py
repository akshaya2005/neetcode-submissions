class MinStack:
    
    def __init__(self):
        self.stack = []
        self.currMin = None
        

    def push(self, val: int) -> None:
        ## the previous min is encoded when you add the new min in
        # print(self.stack)
        if self.currMin == None:
            self.currMin = val
            self.stack.append(0)
        elif val - self.currMin < 0:
            self.stack.append(val - self.currMin)
            self.currMin = val
        else:
            self.stack.append(val - self.currMin)

    def pop(self) -> None:
        # print(self.stack)
        popped = self.stack.pop()
        if not self.stack:
            self.currMin = None
        elif popped < 0:
            self.currMin = self.currMin - popped ## val - (val - currMin)


    
    def top(self) -> int:
        if self.stack[-1] < 0:
            return self.currMin
        return self.stack[-1] + self.currMin
        

    def getMin(self) -> int:
        # print(self.stack)
        return self.currMin
    

"""
currMin = -1
[-1]

"""
