class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        q = deque()

        def addCell(r, c):
            if (r < 0 or c < 0 or r == ROWS or c == COLS or
                (r, c) in visit or grid[r][c] == -1
            ):
                return
            visit.add((r, c))
            q.append([r, c])

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append([r, c])
                    visit.add((r, c))

        dist = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = dist
                for row, col in [(r+1, c), (r-1, c), (r, c-1), (r, c+1)]:
                    if 0 <= row < ROWS and 0 <= col < COLS and (row,col) not in visit and grid[row][col] != -1:
                        visit.add((row, col))
                        q.append([row, col])
            dist += 1