class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        fresh = 0
        rows = len(grid)
        cols = len(grid[0])
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r,c))
                elif grid[r][c] == 1:
                    fresh += 1
        
    
        
        t = 0
        while q and fresh > 0:
       
            qlen = len(q)
            for i in range(qlen):
                r,c = q.popleft()
                for x, y in [(r+1, c), (r-1, c), (r, c-1), (r, c+1)]:
                    if 0 <= x < rows and 0 <= y < cols:
                        if grid[x][y] == 1:
                            grid[x][y] = 2
                            fresh -=1
                            q.append((x,y))
            t += 1
        return t if fresh == 0 else -1

        