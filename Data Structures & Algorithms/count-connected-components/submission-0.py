class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        lis = defaultdict(list)
        for x, y in edges:
            lis[x].append(y)
            lis[y].append(x)
        visited = set()
        def dfs(curr):
            if curr in visited or not lis[curr]:
                return
            visited.add(curr)
            for child in lis[curr]:
                dfs(child)
        
        count = 0
        for i in range(n):
            if i not in visited:
                dfs(i)
                count += 1
        return count
