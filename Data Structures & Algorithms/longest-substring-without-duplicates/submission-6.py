class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        l = 0
        r = 1
        visited = set()
        ## grow the window as long as there are no repeats
        ## when you hit a repeat move l over by 1
        ## start growing the window again
        ## keep a set to keep track of the characters visited so far
        ## everytime you move l, update the length
        maxLen = 0
        for r in range(n):
            while s[r] in visited:
                visited.remove(s[l])
                l += 1
            visited.add(s[r])
            maxLen = max(maxLen, r-l+1)
        return maxLen
            
            


        return maxLen

        