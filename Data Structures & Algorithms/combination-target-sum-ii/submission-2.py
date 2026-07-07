class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        curr = []
        res = []

        def helper(target, index):
            
            if target < 0:
                return
            if target == 0:
                res.append(curr[:])
                return
            ## index + ensures that you do not repeat the number at index i
            for i in range(index, len(candidates)):
                if i > index and candidates[i] == candidates[i-1]:
                    continue
                curr.append(candidates[i])
                helper(target - candidates[i], i + 1)
                curr.pop()
                
        candidates.sort()
        helper(target, 0)
        return res