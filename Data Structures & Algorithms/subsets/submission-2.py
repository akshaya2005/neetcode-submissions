class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ## think of it like dfs
        res = []
        curr = []

        def helper(index):
            ## base case
            if index >= len(nums):
                res.append(curr[:])
                return
            ## all subsets including the element at index
            curr.append(nums[index])
            helper(index + 1)
            ## all subsets excluding the element at the index
            curr.pop()
            helper(index + 1)
        
        helper(0)
        return res
                
                