class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        s = 0
    
        for digit in digits:
            s *= 10
            s += digit
    
        s += 1
        res = deque()
        while s > 0:
            res.appendleft(s % 10)
            s //= 10
        
        return list(res)

            

        