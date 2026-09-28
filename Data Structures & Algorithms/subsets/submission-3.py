class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        curr = []

        def helper(index):
            if index >= len(nums):
                res.append(curr[:])
                return
            
            ## subsets including this element
            curr.append(nums[index])
            helper(index + 1)

            ## subsets not including this element
            curr.pop()
            helper(index + 1)
        
        helper(0)
        return res
            
    