class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        curr = []
        res = []

        def helper(index):
            if index >= len(nums):
                res.append(curr[:])
                return
            
            curr.append(nums[index])
            helper(index + 1)
            curr.pop()
            while index < len(nums) - 1 and nums[index] == nums[index + 1]:
                index += 1
            helper(index + 1)
        
        nums.sort()
        helper(0)
        return res
        
        

        