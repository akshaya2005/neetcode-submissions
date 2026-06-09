class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [0] * len(nums)

        for i in range(len(nums)):
            maxlen = 0
            for j in range(i):
                if nums[j] < nums[i]:
                    maxlen = max(maxlen, dp[j])

            dp[i] = maxlen + 1
        print(dp)
        return max(dp)
                

        