class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
    
        res = []
        curr = []

        def helper(index):
            if len(nums) <= index:
                res.append(curr[:])
                return
            
            curr.append(nums[index])
            helper(index + 1)
            curr.pop()
            helper(index + 1)
        
        helper(0)
        return res
            

        