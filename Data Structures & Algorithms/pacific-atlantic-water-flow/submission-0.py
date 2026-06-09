class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ## dfs from the outside in
        rows, cols = len(heights), len(heights[0])
        pac, atl = set(), set()
        def canReach(r, c, visited, prev):
            if r < 0 or c < 0  or r >= rows or c >= cols or heights[r][c] < prev or (r,c) in visited:
                return
            visited.add((r,c))
            canReach(r+1, c, visited, heights[r][c])
            canReach(r-1, c, visited, heights[r][c])
            canReach(r, c+1, visited, heights[r][c])
            canReach(r, c-1, visited, heights[r][c])
            
        
        res = []
        for c in range(cols):
            canReach(0, c, pac, heights[0][c])
            canReach(rows - 1, c, atl, heights[rows-1][c])
        for r in range(rows):
            canReach(r, 0, pac, heights[r][0])
            canReach(r, cols-1, atl, heights[r][cols - 1])


        for i in range(rows):
            for j in range(cols):
                if (i, j) in atl and (i, j) in pac:
                    res.append((i, j))
        return res
        

                
        

        