class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        curr = []

        def helper(nums, index, target):
            if target < 0:
                return
            if target == 0:
                res.append(curr[:])
            
            for i in range(index, len(nums)):
                if i > index and nums[i] == nums[i-1]:
                    continue
                curr.append(nums[i])
                helper(nums, i + 1, target - nums[i])
                curr.pop()
            
        nums.sort()
        helper(nums, 0, target)
        return res

            