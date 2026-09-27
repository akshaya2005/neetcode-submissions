class Solution:
    def reverse(self, x: int) -> int:
        s = 0
        num = abs(x)
        
       
        while num > 0:
            digit = num % 10
            s *= 10
            s += digit
            num //= 10
        
        if s < -2**31 or s > 2**31-1:
            return 0
        return -s if x < 0 else s
        