class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        ## dp should store the max you can get if you choose to 
        ## rob this house
        ## 
        dp = [0] * n
        if n < 2:
            return nums[0]
        dp[0] = nums[0]
        dp[1] = max(nums[1], nums[0])
        mx = max(dp[0], dp[1])
        for i in range(2, n):
            dp[i] = max(dp[i-1], nums[i] + dp[i-2])
            mx = max(mx, dp[i])
        
        return mx

            

        