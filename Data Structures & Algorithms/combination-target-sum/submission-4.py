class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        curr = []

        def helper(index, target):
            if index >= len(nums) or target < 0:
                return 
            if target == 0:
                res.append(curr[:])
            
            for i in range(index, len(nums)):
                curr.append(nums[i])
                helper(i, target - nums[i])
                curr.pop()
        
        helper(0, target)
        return res