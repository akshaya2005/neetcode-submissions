class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ## number days between i'th day and a hotter day
        res = [0] * len(temperatures)
        stack = [(temperatures[0], 0)]
        for r in range(1, len(temperatures)):
            while stack and stack[-1][0] < temperatures[r]:
                popped = stack.pop()
                res[popped[1]] = r - popped[1]
            
            
            
            stack.append((temperatures[r], r))
        
        return res
            
        