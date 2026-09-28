class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
    
        res = []
       
        if len(nums) == 1:
            return [nums[:]]
        
        for i in range(len(nums)):
            first = nums.pop(0)
            perms = self.permute(nums)
            for perm in perms:
                perm.append(first)
            nums.append(first)
            for perm in perms:
                res.append(perm[:])
        
       
        return res


        