class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        stack = []
        intervals = sorted(intervals, key = lambda x:(x[0], x[1]))
        for start, end in intervals:
            if stack:
                if stack[-1][0] <= start <= stack[-1][1]:
                    prev = stack.pop()
                    stack.append([min(prev[0], start), 
                    max(prev[1], end)])
                    continue
            stack.append([start, end])
        return stack
        