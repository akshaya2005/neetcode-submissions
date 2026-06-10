class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        print(nums)
        n = len(nums)
        res = []
        s = 0
        while s < n:
            

            i = s + 1
            j = n - 1

            while i < j:
                if nums[i] + nums[j] + nums[s] == 0:
                    res.append([nums[s], nums[i], nums[j]])
                    i += 1
                    j -= 1
                elif nums[i] + nums[j] + nums[s] < 0:
                    i += 1
                else:
                    j -= 1
                while s + 1 < i < n and nums[i] == nums[i - 1]:
                    i += 1
                while s + 1 < j < n - 1 and nums[j] == nums[j + 1]:
                    j -= 1
            s += 1
            while n > s > 0 and nums[s] == nums[s-1]:
                s += 1

        
        return res
                    

        