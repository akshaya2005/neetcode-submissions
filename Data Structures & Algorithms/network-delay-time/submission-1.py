class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        ## dijkstra's from source k
        distMap = {i : float('inf') for i in range(1, n + 1)}
        distMap[k] = 0
        adj = defaultdict(list)
        for edge in times:
            u, v, time = edge
            adj[u].append([v, time])
        visited = set()
        minheap = [[0, k]]
        
        while minheap:
            currDist, currVert = heapq.heappop(minheap)
            if currVert not in visited:
                visited.add(currVert)
                for child in adj[currVert]:
                    heapq.heappush(minheap, [child[1] + currDist, child[0]])
                    distMap[child[0]] = min(distMap[child[0]], child[1] + currDist)
        
        return max(list(distMap.values())) if len(visited) == n else -1