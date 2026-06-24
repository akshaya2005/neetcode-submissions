class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for char in s:

            if char == "(" or char == "{" or char == "[":
                stack.append(char)
            else:
                if not stack:
                    return False
                comp = stack.pop()
                if char == "}" and comp != "{":
                    return False
                
                if char == "]" and comp != "[":
                    return False
                
                if char == ")" and comp != "(":
                    return False

        
        return len(stack) == 0
        
        