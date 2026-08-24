class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        visited = set()
        def dfs(row, col):
            if row >= ROWS or row < 0 or col < 0 or col >= COLS or grid[row][col] != "1" or (row, col) in visited:
                return
            visited.add((row, col))
            for r, c in [(row+1, col), (row, col+1), (row-1, col), (row, col-1)]:
                dfs(r, c)

        numIslands = 0
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == "1" and (i, j) not in visited:
                    dfs(i, j)
                    numIslands += 1

        return numIslands

