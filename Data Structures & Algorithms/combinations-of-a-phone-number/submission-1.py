class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: 
            return []
        mp = {}
        mp['2'] = ['a', 'b', 'c']
        mp['3'] = ['d', 'e', 'f']
        mp['4'] = ['g', 'h', 'i']
        mp['5'] = ['j', 'k', 'l']
        mp['6'] = ['m', 'n', 'o']
        mp['7'] = ['p', 'q', 'r', 's']
        mp['8'] = ['t', 'u', 'v']
        mp['9'] = ['w', 'x', 'y', 'z']

        ## needs a loop because we include everything here
        res = []
        curr = []
        def dfs(index):
            if len(curr) == len(digits) and len(curr) > 0:
                res.append("".join(curr))
                return
            
            for char in mp[digits[index]]:
                curr.append(char)
                dfs(index + 1)
                curr.pop()
        
        dfs(0)
        return res
