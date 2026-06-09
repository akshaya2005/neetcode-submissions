class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        numberMap = defaultdict(list)
        p = 0
        for i in range(2, 10):
            letters = 3
            if i == 7 or i == 9:
                letters = 4
            for j in range(letters):
                numberMap[chr(i + ord('0'))].append(chr(p + ord('a')))
                p += 1
        print(numberMap)

        res = []
        curr = []
        def helper(index):
            if not digits:
                return
            if len(curr) == len(digits):
                ## append the final string to res
                res.append("".join(curr))
                return
            ## adding the current character for the number to the string
            for letter in numberMap[digits[index]]:
                curr.append(letter)
                helper(index + 1)
                curr.pop()
        
        helper(0)
        return res
        


        