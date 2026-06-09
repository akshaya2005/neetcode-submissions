class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [nums[:]]
        res = []
        for i in range(len(nums)):
            n = nums.pop()
            perms = self.permute(nums)
            print(res)
            for perm in perms:
                perm.append(n)
            nums.insert(0, n)
            res.extend(perms)
        return res
        