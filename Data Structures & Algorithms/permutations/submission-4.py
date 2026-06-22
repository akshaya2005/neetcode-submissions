class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        self.backtrack([], nums, set())
        return self.res

    
    def backtrack(self, perm: List[int], nums:List[int], visited):
        if len(perm) == len(nums):
            print(perm)
            self.res.append(perm[:])
            return
        
        for i in range(len(nums)):
            if not nums[i] in visited:
                perm.append(nums[i])
                visited.add(nums[i])
                self.backtrack(perm, nums, visited)
                perm.pop()
                visited.remove(nums[i])
     



        