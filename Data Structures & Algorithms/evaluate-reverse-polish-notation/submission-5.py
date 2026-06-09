class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def evaluate(symbol, num1, num2):
            if symbol == "+":
                return num1 + num2
            if symbol == "-":
                return num1 - num2
            if symbol == "*":
                return num1 * num2
            if symbol == "/":
                return int(num1 / num2)
        
        
    
        symbols = set(["+", "-", "*", "/"])
        stack = []
        for i in range(len(tokens)):
            if tokens[i] not in symbols:
                stack.append(int(tokens[i]))
            else:
                num2 = stack.pop()
                num1 = stack.pop()
                stack.append(evaluate(tokens[i], num1, num2))
            print(tokens[i])
            print(stack)
        return stack[-1]
       
            

            



        