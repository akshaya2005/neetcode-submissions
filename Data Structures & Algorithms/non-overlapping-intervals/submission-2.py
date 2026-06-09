class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        res = 0
        prevEnd = intervals[0][1]

        for start, end in intervals[1:]:
            if start >= prevEnd: ## the two intervals are non-overlapping
                prevEnd = end
            else:  ## overlapping interval, remove the interval with the greater end
                res += 1
                prevEnd = min(end, prevEnd)
        return res  
    ## [1, 100], [1, 12], [11, 22],       