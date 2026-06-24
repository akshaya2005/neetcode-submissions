class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for char in tokens:
            
            if char == "+" or char == "-" or char == "*" or char == "/":
                num1 = stack.pop()
                num2 = stack.pop()

                if char == "+":
                    stack.append(num1 + num2)
                if char == "-":
                    stack.append(num2 - num1)
                if char == "/":
                    stack.append(int(num2 / num1))
                if char == "*":
                    stack.append(num1 * num2)

            else:
                stack.append(int(char))
            
        return stack.pop()
        
        
        
        