class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        ## edge map
        edgeMap = defaultdict(list)
        for start, end in edges:
            edgeMap[start].append(end)
            edgeMap[end].append(start)

        visited = set()
        def dfs(node, parent):
            if node in visited:
                return
            
            visited.add(node)
            for end in edgeMap[node]:
                ## ignore reverse edges
                if parent == end:
                    continue
                
                dfs(end, node)
            
            return

        count = 0
        for i in range(n):
           
            if len(visited) < n and i not in visited:
                dfs(i, -1)
                count += 1
                # visited.clear()
        
        return count

        