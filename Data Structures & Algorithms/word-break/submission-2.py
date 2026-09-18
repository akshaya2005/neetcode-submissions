class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False for _ in range(len(s))]
        wordSet = set(wordDict)
        

        for i in range(len(s)):
            for j in wordSet:
                ## split into two sections
                ## w1 = 0 : i - len(word from wordSet)
                ## w2 = i - len(word from wordSet) : i
                ## dp[w1] should be true and w2 must be in wordSet
                bp = i - len(j)
                if bp >= -1:
                    w2 = s[bp + 1:i + 1]
                    if w2 in wordSet and (dp[bp] or bp == -1):
                        dp[i] = True
                        break
        print(dp)
        return dp[-1]
                

        