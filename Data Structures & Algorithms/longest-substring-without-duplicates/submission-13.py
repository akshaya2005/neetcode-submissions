class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()
        l = 0
        maxWindow = 0
        for r in range(len(s)):
            if s[r] not in window:
                window.add(s[r])
                maxWindow = max(maxWindow, r - l + 1)
            ## s[r] is in the window
            else:
                while s[l] != s[r]:
                    window.remove(s[l])
                    l += 1
                l += 1
        return maxWindow
            


        