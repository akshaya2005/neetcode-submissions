class Solution:
    def partition(self, s: str) -> List[List[str]]:
        part = []
        res = []
        ## j is start and i is end
        def dfs(j, i):
            if i >= len(s):
                if i == j:
                    res.append(part.copy())
                return 
            
            if self.isPalindrome(s, j, i):
                part.append(s[j : i + 1])
                dfs(i + 1, i + 1)
                part.pop()
            ## if s[j:i] is not a substring, extend the window by one
            dfs(j, i + 1)
        
        dfs(0, 0)
        return res

    def isPalindrome(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l,r = l + 1, r - 1
        return True

        