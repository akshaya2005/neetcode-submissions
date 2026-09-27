class Solution:
    def isHappy(self, n: int) -> bool:
        while True:
            num = n
            s = 0
            while num > 0:
                s += (num % 10) ** 2
                num //= 10
            n = s
            if n == 1 or (n < 10 and n != 1):
                break
        
        if n == 1:
            return True
        else:
            return False
