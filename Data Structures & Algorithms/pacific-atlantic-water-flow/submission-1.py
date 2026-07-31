class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ## dfs from the outside in
        rows, cols = len(heights), len(heights[0])
        pac, atl = set(), set()
        def canReach(r, c, visited, prev):
            if r < 0 or r >= rows or c < 0 or c >= cols or (r, c) in visited or heights[r][c] < prev:
                return
            visited.add((r,c))
            for row, col in [(r+1, c), (r-1, c), (r, c-1), (r, c+1)]:
                canReach(row, col, visited, heights[r][c])
            
            return
        ## left
        for r in range(rows):
            canReach(r, 0, pac, heights[r][0])
            canReach(r, cols - 1, atl, heights[r][cols - 1])
        for c in range(cols):
            canReach(0, c, pac, heights[0][c])
            canReach(rows - 1, c, atl, heights[rows-1][c])


        res = []
        for i in range(rows):
            for j in range(cols):
                if (i,j) in pac and (i,j) in atl:
                    res.append([i,j])
        return res
                    

                
        