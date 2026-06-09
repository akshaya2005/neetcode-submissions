class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        index = {query : index for index, query in enumerate(queries)}

       
        minheap = []
        res = {}
        i = 0
        for q in sorted(queries):
            
            while i < len(intervals) and intervals[i][0] <= q:
                heapq.heappush(minheap, [intervals[i][1] - intervals[i][0] + 1, intervals[i][1]])
                i += 1
            while minheap and minheap[0][1] < q:
                heapq.heappop(minheap)
            res[q] = minheap[0][0] if minheap else -1
        return [res[q] for q in queries]



        