class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        
        def dfs(row, col, arr):
            if row >= rows or col >= cols or row < 0 or col < 0 or (row, col) in visited:
                return 0
            if grid[row][col] == 0:
                return 0
            visited.add((row, col))
            arr[0] += 1
            for i, j in [(row+1, col), (row-1, col), (row, col+1), (row, col-1)]:
                dfs(i, j, arr)
            return arr[0]
        
        maxSize = 0
        for r in range(rows):
            for c in range(cols):
                arr = [0]
                if (r,c) not in visited:
                    size = dfs(r, c, arr)
                    maxSize = max(maxSize, arr[0])
                    
                
        return maxSize

                

