from functools import lru_cache
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        @lru_cache
        def dfs(i, buying):
            ## base case no more profit to be made
            if i >= len(prices):
                return 0
            ## skip today
            cooldown = dfs(i + 1, buying)

            if buying:
                buy = dfs(i + 1, not buying) - prices[i]
                return max(buy, cooldown)
            else:
                sell = dfs(i+2, not buying) + prices[i]
                return max(cooldown, sell)

        return dfs(0, True)