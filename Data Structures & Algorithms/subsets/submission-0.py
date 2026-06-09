class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        curr = []

        def helper(index):
            if index >= len(nums):
                res.append(curr[:])
                return
            ## either choose to include the current number or not
            curr.append(nums[index])
            helper(index + 1)
            curr.pop()
            helper(index + 1)
        
        helper(0)
        return res

        