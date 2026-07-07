class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        curr = []
        res = []

        def helper(target, index):
            if target < 0:
                return
            if target == 0:
                res.append(curr[:])
                return
            
            for i in range(index, len(nums)):
               
                curr.append(nums[i])
                helper(target - nums[i], i)
                curr.pop()
        helper(target, 0)
        return res
            

        
        