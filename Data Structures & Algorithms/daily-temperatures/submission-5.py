class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)

        stack = [(temperatures[0],0)]
        for i in range(len(temperatures)):
            while stack and stack[-1][0] < temperatures[i]:
                popped = stack.pop()
                res[popped[1]] = i - popped[1]
            stack.append((temperatures[i], i))
        return res
        
