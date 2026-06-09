class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adjList = defaultdict(list)
        for x,y in edges:
            adjList[x].append(y)
            adjList[y].append(x)
        
        visited = set()
        def dfs(curr, par):
            if curr in visited:
                return False
            visited.add(curr)
            for child in adjList[curr]:
                if child == par:
                    continue
                if not dfs(child, curr):
                    return False
            # visited.remove(curr)
            return True
        
        
        return dfs(0, -1) and len(visited) == n

