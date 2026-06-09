class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        ## work backwards
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True ## to ensure that the first break from the end is captured
        for i in range(len(s) - 1, -1, -1):
            for word in wordDict:
                l = len(word)
                if i + l <= len(s):
                    if s[i : i + l] == word:
                        dp[i] = dp[i + l]
                if dp[i]:
                    break  
        return dp[0]

        