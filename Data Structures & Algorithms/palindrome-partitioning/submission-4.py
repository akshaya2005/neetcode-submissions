class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        curr = []
        palindrome = ""
        def helper(j, i):
            if i >= len(s):
                if i == j:
                    res.append(curr[:])
                return
            
            if isPalindrome(s, j, i):
                curr.append(s[j : i + 1])
                ## start a new palindromic partition
                helper(i+1, i+1)
                curr.pop()
            
            helper(j, i+1)
        
        def isPalindrome(s, l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        helper(0, 0)
        return res
            
            

        