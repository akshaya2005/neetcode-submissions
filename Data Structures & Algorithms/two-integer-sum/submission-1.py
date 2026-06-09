class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diffs = {}
        indices = {}
        for i in range(len(nums)):
            indices[nums[i]] = i
        
        for i in range(len(nums)):
            tar = target - nums[i]
            if tar in indices and indices[tar] != i:
                return [i, indices[tar]]