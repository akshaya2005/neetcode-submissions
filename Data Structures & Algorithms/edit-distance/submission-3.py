class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n = len(word1)
        m = len(word2)
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        ## dp[i, j] is the minimum number of ops required to turn
        ## word1[:i] into word2[:j]
        ## base case
        ## to transform the empty string into another string of length 
        ## j you need j transforms
        dp[0] = [i for i in range(n+1)]
        for j in range(m+1):
            dp[j][0] = j

        for i in range(1, m+1):
            for j in range(1, n+1):
                if word1[j-1] == word2[i-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
        print(dp)
        return dp[-1][-1]
