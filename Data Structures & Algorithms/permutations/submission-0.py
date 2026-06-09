class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        curr = []
        pick = [False] * len(nums)
        def helper():
            print(curr, nums)
            if len(curr) == len(nums):
                res.append(curr[:])
                return
            
            
            for i in range(len(nums)):
                if not pick[i]:
                    curr.append(nums[i])
                    pick[i] = True
                    helper()
                    curr.pop()
                    pick[i] = False
        
        helper()
        return res