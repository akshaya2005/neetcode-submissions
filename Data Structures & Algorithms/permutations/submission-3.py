class Solution:
    res = []
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [nums[:]]
        res = []
        for i in range(len(nums)):
            first = nums.pop(0)
            perms = self.permute(nums)
            for perm in perms:
                perm.append(first)
            nums.append(first)
            res.extend(perms)
        
        return res



        