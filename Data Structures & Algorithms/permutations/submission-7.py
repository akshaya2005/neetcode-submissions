class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
    
        visited = set()
        res = []
        curr = []
        def helper():
            if len(nums) == len(curr):
                res.append(curr[:])
                return
            for i in range(len(nums)):
                if nums[i] not in visited:
                    curr.append(nums[i])
                    visited.add(nums[i])
                    helper()
                    curr.pop()
                    visited.remove(nums[i])
        helper()
        return res