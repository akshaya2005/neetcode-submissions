class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [0 for _ in range(n+1)]
        ## cost is zero to get to the zero'th step
        dp[0] = 0
        ## cost is zero to get to the first step
        dp[1] = 0
        for i in range(2, n+1):
            dp[i] = min(dp[i - 1] + cost[i-1], dp[i - 2] + cost[i-2])
        print(dp)
        return dp[-1]
        

        