class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        for start, end, time in times:
            adj[start].append((end, time))

        ## s to all other nodes shortest path- this is dijkstra's
        
        pq = []
        ## pq contains a vertex-distance tuples
        heapq.heappush(pq, (0, k))

        visited = set()
        t = 0
        while pq and len(visited) < n:
            d, curr = heapq.heappop(pq)
            if curr in visited:
                continue
            visited.add(curr)
            t = d
            for nei, neiDist in adj[curr]:
                if nei not in visited:
                    
                    heapq.heappush(pq, (neiDist + d, nei))
        
        return -1 if len(visited) < n else t

            



        