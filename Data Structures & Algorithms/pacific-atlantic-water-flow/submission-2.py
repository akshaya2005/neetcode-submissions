class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS = len(heights)
        COLS = len(heights[0])
        pacific = set()
        atlantic = set()
        # the cells have water


        ## two loops iterating over the edges
        ## top left- pacific
        ## bottom right- atlantic

        def canFlow(row, col, prev, visited):
         
            if row >= ROWS or col >= COLS or row < 0 or col < 0 or heights[row][col] < prev or (row, col) in visited:
                return
            visited.add((row, col))
            canFlow(row+1, col, heights[row][col], visited)
            canFlow(row-1, col, heights[row][col], visited)
            canFlow(row, col-1, heights[row][col], visited)
            canFlow(row, col+1, heights[row][col], visited)
            
        

        for i in range(ROWS):
            canFlow(i, 0, heights[i][0], pacific)
            canFlow(i, COLS - 1, heights[i][COLS - 1], atlantic)
        for j in range(COLS):
            canFlow(0, j, heights[0][j], pacific)
            canFlow(ROWS - 1, j, heights[ROWS - 1][j], atlantic)
        print(pacific, atlantic)
        result = []
        for i in range(ROWS):
            for j in range(COLS):
                if (i,j) in pacific and (i,j) in atlantic:
                    result.append((i,j))
        return result
            

        