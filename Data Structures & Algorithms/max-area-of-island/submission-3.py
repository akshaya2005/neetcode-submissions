class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        rows, cols = len(grid), len(grid[0])
        visited = set()
        def dfs(r, c):
            if r < 0 or c < 0 or r >= rows or c >= cols or (r,c) in visited:
                return 0
            if grid[r][c] == 0:
                return 0
        
            visited.add((r,c))
    
            return 1 + dfs(r + 1, c) + dfs(r, c + 1) + dfs(r - 1, c) + dfs(r, c - 1)
            
        
        area = 0
        array = []
        for r in range(rows):
            for c in range(cols):
                if (r,c) not in visited and grid[r][c] == 1:
                    area = max(area, dfs(r,c))
        # print(array)
        return area
                

