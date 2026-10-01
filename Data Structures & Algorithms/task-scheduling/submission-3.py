class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        ## count frequencies and then pop and add to the final list
        counts = Counter(tasks)
        heap = [-cnt for cnt in counts.values()]
        q = deque()

        heapq.heapify(heap)
        time = 0
        while heap or q:
            time += 1
            if heap:
                curr = heapq.heappop(heap)
                curr += 1
                if curr:
                    q.append([curr, time + n])

            if q and q[0][1] == time:
                heapq.heappush(heap, q.popleft()[0])
        
        return time


        