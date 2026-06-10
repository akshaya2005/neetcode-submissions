class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ## use a hashmap
        lot = {}
        n = len(s)
        i = 0
        j = 0
        maxLen = 0


        for j in range(n):
        
            if s[j] in lot and lot[s[j]] >= i:
                i = lot[s[j]] + 1
            else:
                maxLen = max(maxLen, j - i + 1)
            lot[s[j]] = j
           
        return maxLen




        
        