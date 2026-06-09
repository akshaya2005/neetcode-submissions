class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        dp = [[0,0] for _ in range(len(nums))]

        dp[0][0] = nums[0]
        dp[0][1] = nums[0]

        maxProd = nums[0]

        for i in range(1, len(nums)):
            dp[i][0] = max(dp[i-1][1] * nums[i], dp[i-1][0] * nums[i], nums[i])
            dp[i][1] = min(dp[i-1][0] * nums[i], dp[i-1][1] * nums[i], nums[i])

            maxProd = max(maxProd, dp[i][0])
        return maxProd
            
        