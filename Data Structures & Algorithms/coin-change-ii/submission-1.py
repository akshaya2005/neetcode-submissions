class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [[0 for _ in range(amount + 1)] for _ in range(len(coins))]

        for i in range(len(coins)):
            dp[i][0] = 1
        
        for c in range(len(coins)):
            for a in range(amount + 1):
                dp[c][a] = dp[c-1][a]
                if a - coins[c] >= 0:
                    dp[c][a] += dp[c][a-coins[c]]

        return dp[-1][-1]
        