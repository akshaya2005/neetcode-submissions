class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []
        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            j = i + 1
            k = n - 1
        
            while j < k:
                total = nums[i] + nums[j] + nums[k]
                if total == 0:
                    res.append([nums[i], nums[j], nums[k]])
                if total < 0:
                    j += 1
                    continue
                if total > 0:
                    k -= 1
                    continue
                j += 1
                while nums[j] == nums[j-1] and j < k:
                    j += 1
                
        return res
            