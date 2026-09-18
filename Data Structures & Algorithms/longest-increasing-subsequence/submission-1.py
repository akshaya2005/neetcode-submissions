class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1 for _ in range(len(nums))]
      
        globalMax = float('-inf')


        for i in range(len(nums)):
            for j in range(0, i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
            globalMax= max(globalMax, dp[i])
        print(dp)
        return globalMax
        
        

        