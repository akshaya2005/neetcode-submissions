class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        number1 = 0
        number2 = 0

        for char in num1:
            number1 *= 10
            number1 += (ord(char) - ord('0'))
            
        
        for char in num2:
            number2 *= 10
            number2 += (ord(char) - ord('0'))
            
        

        prod = number2 * number1
        if prod == 0:
            return "0"
        res = ""
        while prod > 0:
            digit = prod % 10
            res = str(digit) + res
            prod //= 10
        
        return res

            
        