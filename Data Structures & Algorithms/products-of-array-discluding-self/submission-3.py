class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        n = len(nums)
        pref = [1 for _ in range(n)]
        suff = [1 for _ in range(n)]

        for i in range(1, n):
            pref[i] = pref[i-1] * nums[i-1]
        
        for i in range(n-2, -1, -1):
            suff[i] = suff[i+1] * nums[i+1]
        
        for i in range(n):
            res.append(pref[i] * suff[i])
        return res
        



        



        