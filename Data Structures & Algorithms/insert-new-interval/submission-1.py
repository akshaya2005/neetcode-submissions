class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        stack = []
        for i, interval in enumerate(intervals):
            ## new interval fully less than
            if newInterval[1] < interval[0]:
                stack.append(newInterval)
                return stack + intervals[i:]
            ## new interval fully greater than
            elif newInterval[0] > interval[1]:
                stack.append(intervals[i])
            ## overlap
            else:
                newInterval = [min(newInterval[0], interval[0]), 
                                max(newInterval[1], interval[1])]
        stack.append(newInterval)
        return stack
           

            

        