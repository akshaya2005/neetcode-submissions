class Solution:
    def rob(self, nums: List[int]) -> int:
        
        def robHelper(arr):
            if len(arr) < 2:
                return arr[0]
            maxAmt = 0
            n = len(arr)
            dp = [0] * n

            dp[0] = arr[0]
            dp[1] = max(arr[0], arr[1])
            maxAmt = dp[1]
            for i in range(2, n):
                dp[i] = max(dp[i-2] + arr[i], dp[i-1])
                maxAmt = max(maxAmt, dp[i])
            
            return maxAmt
        
        if len(nums) == 1:
            return nums[0]
        return max(robHelper(nums[:-1]), robHelper(nums[1:]))