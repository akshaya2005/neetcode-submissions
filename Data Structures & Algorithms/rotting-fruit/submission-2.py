class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ## multi source bfs
        rows = len(grid)
        cols = len(grid[0])
        q = deque()
        visited = set()
        fresh = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    q.append((i, j))
                if grid[i][j] == 1:
                    fresh += 1
                
        count = 0
        while q and fresh > 0:
            count += 1
            qlen = len(q)
            for i in range(qlen):
                row, col = q.popleft()
                for r, c in [(row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)]:
                        if 0 <= r < rows and 0 <= c < cols and grid[r][c] == 1 :
                            grid[r][c] = 2
                            fresh -= 1
                            q.append((r, c))

                            


        return count if fresh == 0 else - 1
            
        