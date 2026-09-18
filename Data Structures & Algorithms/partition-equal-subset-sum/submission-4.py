class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        t = sum(nums)
        if t % 2 != 0:
            return False
        t = t // 2
        n = len(nums)
        dp = [[False] * (t + 1) for _ in range(n+1)]
        ## dp[i][j] represents whether you can obtain value of j with the first i numbers
        for i in range(n+1):
            dp[i][0] = True
        
        for i in range(1, n+1):
            for j in range(1, t + 1):
                if nums[i-1] <= j:
                    dp[i][j] = dp[i-1][j] or dp[i-1][j - nums[i-1]]
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[n][t]



        

        