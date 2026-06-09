class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        visited = {}
        l = 0
        r = 1
        ## grow the window as long as there are no repeats
        ## when you hit a repeat move l over by 1
        ## start growing the window again
        ## keep a set to keep track of the characters visited so far
        ## everytime you move l, update the length
        res = 0
        
        for r in range(n):
            if s[r] in visited:
                l = max(visited[s[r]] + 1, l) ## never let l move back
            visited[s[r]] = r
            res = max(res, r-l+1)
        return res
    
            


        return maxLen

        