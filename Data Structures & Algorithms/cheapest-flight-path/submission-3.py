class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        ## Dijkstra's
        INF = float('inf')
        adj = defaultdict(list)
        ## initialize dist map
        dist = [[INF] * (k+2) for _ in range(n)]
        
        
        ## build adjacency list
        for u, v, cst in flights:
            adj[u].append((v, cst))
       
        ## initialize minheap
        dist[src][0] = 0
        pq = [(0, src, -1)]

        while pq:
            cst, node, stops = heapq.heappop(pq)
            if node == dst:
                return cst

            if stops == k or cst > dist[node][stops + 1]:
                continue
            
            for nei, neiCost in adj[node]:
                totalCost = cst + neiCost
                nextStops = stops + 1
                if totalCost < dist[nei][nextStops+1]:
                    dist[nei][nextStops+1] = totalCost
                    heapq.heappush(pq, (totalCost, nei, nextStops))
            
        return -1

                

        