class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        dp = [amount + 1 for _ in range(amount+1)]
        dp[0] = 0


        for i in range(1,amount + 1):
            for c in coins:
                index = i - c 
                if index >= 0:
                    dp[i] = min(dp[i], dp[index] + 1)

        print(dp)
        return dp[-1] if dp[-1] != amount + 1 else -1          

                
                
        