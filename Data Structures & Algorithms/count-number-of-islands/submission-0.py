class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
    
        count = 0
        rows, cols = len(grid), len(grid[0])
        def dfs(r, c):
            ## do not continue search if board[r][c] == 0
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == "0":
                return
            
            ## marking as visited
            grid[r][c] = "0"
            for x, y in [(r, c+1), (r+1, c), (r, c-1), (r-1, c)]:
                dfs(x, y)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    dfs(r, c)
                    count += 1
        return count
        
            

