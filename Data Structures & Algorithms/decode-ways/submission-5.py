class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [0 for _ in range(n)]
        dp[0] = 0 if s[0] == '0' else 1
        if len(s) > 1:
            if (s[0] == '1' or (s[0] == '2' and s[1] <= '6')):
                if s[1] == '0':
                    dp[1] = 1
                else:
                    dp[1] = 2
            elif s[0] == '0' or s[1] == '0':
                dp[1] = 0
            else:
                dp[1] = 1
            
            
            
 
        for i in range(2, n):
            if s[i-1] == '1' or (s[i-1] == '2' and s[i] <= '6'):
                dp[i] += dp[i-2]
            if s[i] != '0':
                dp[i] += dp[i-1]
        print(dp)
        return dp[-1]


        