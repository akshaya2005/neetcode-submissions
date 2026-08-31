class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        ## cannot do this the same way as the directed edge cycle detection because edge (0,1) (1,0) would be treated as a cycle
        visited = set()
        edgeMap = defaultdict(list)
        for start, end in edges:
            edgeMap[start].append(end)
            edgeMap[end].append(start)

        def dfs(node, par):
            if node in visited:
                return False
            
            
            visited.add(node)
            for end in edgeMap[node]:
                if end == par:
                    continue
                if not dfs(end, node):
                    return False
        

            return True
        
        return dfs(0, -1) and len(visited) == n

            


        