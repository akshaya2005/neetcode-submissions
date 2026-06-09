class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        curr = []
        def helper(cur, nums, index, target):
            if target < 0:
                return
            print(target, curr)
            if target == 0:
                res.append(curr[:])
                return 
            for i in range(index, len(nums)):
                curr.append(nums[i])
                helper(nums[i], nums, i, target - nums[i])
                curr.pop()
        
        helper(nums[0], nums, 0, target)
        return res

        