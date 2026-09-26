class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        ## [(30, 0)]
        ## if temperatures[r] > any of the stuff in the stack pop
        ## all the ones that are smaller and set res[index] = r - index
        stack = [(temperatures[0], 0)]
        for r in range(1, len(temperatures)):
            while stack and stack[-1][0] < temperatures[r]:
                popped = stack.pop()
                res[popped[1]] = r - popped[1]
            stack.append((temperatures[r], r))
        return res
        
