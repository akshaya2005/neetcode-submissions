class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        curr = []
      
        def helper(i):
            if i >= len(s):
                res.append(curr[:])
                return
            
            for j in range(i, len(s)):
                if isPalindrome(s, i, j):
                    curr.append(s[i:j+1])
                ## start a new palindromic partition
                    helper(j+1)
                    curr.pop()
            
      
        
        def isPalindrome(s, l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        helper(0)
        return res
            
            

        