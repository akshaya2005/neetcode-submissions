class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        neg = [0] * n
        pos = [0] * n
        neg[0] = nums[0]
        pos[0] = nums[0]

        if n == 1:
            return nums[0]
        maxProd = float('-inf')
        for i in range(1,n):
            pos[i] = max(pos[i-1]*nums[i], neg[i-1]*nums[i], nums[i])
            neg[i] = min(pos[i-1]*nums[i], neg[i-1]*nums[i], nums[i])
            maxProd = max(maxProd, pos[i])
     
        return maxProd
        
        