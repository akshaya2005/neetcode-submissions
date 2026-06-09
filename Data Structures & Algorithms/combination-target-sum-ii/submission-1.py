class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        curr = []
        res = []

        def helper(nums, index, target):
            if target < 0:
                return
            if target == 0:
                res.append(curr[:])
                return
            
            for i in range(index, len(nums)):
                if (i > index and nums[i] == nums[i - 1]):
                    continue
                curr.append(nums[i])
                helper(nums, i + 1, target - nums[i])
                curr.pop()
            
        candidates.sort()
        helper(candidates, 0, target)
        return res
        