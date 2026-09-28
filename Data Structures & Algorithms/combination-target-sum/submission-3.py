class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        curr = []
        def helper(index, target):
            if target == 0:
                res.append(curr[:])
                return
            if index >= len(nums) or target < 0:
                return 
            
            
            for i in range(index, len(nums)):
                curr.append(nums[i])
                helper(i, target - nums[i])
                curr.pop()
        
        helper(0, target)
        return res

        