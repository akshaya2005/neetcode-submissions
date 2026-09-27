class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        arrayTotal = sum(nums)
        expTotal = (n*(n+1)) // 2

        return expTotal - arrayTotal

        

        