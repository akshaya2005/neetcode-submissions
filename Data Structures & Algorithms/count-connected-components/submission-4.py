class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        ## construct adjacency list
        adj = defaultdict(list)

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        visited = set()
        def dfs(curr, parent):
            if curr in visited:
                return
            visited.add(curr)
            for nei in adj[curr]:
                if (nei != parent):
                    dfs(nei, curr)
            return
        
        count = 0
        for i in range(n):
            if i not in visited:
                dfs(i, -1)
                count += 1
        return count

        

        