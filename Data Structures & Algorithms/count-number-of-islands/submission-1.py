class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:


        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        
        def dfs(row, col, size):
            if row >= rows or col >= cols or row < 0 or col < 0 or (row, col) in visited:
                return size
            if grid[row][col] == "0":
                return size
            visited.add((row, col))
            size += 1
            for i, j in [(row+1, col), (row-1, col), (row, col+1), (row, col-1)]:
                dfs(i, j, size)

            return size
        
        count = 0
        for r in range(rows):
            for c in range(cols):
                if (r,c) not in visited:
                    if dfs(r, c, 0) > 0:
                        count += 1
        return count


                    

            
        

            

                

            
        