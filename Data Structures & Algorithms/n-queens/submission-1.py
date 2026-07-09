class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col = set()
        posDiag = set() # r + c
        negDiag = set() # r - c
        res = []
        curr = [["."] * n for _ in range(n)]
        ## back track along the rows
        def backtrack(r):
            if r == n:
                res.append(["".join(row) for row in curr])
                return
            ## trying every column in the FIRST row for the placement 
            ## of the first queen
            for c in range(n):
                if c in col or (r+c) in posDiag or (r-c) in negDiag:
                    continue
                col.add(c)
                negDiag.add(r-c)
                posDiag.add(r+c)
                curr[r][c] = "Q"
                backtrack(r+1)
                col.remove(c)
                posDiag.remove(r+c)
                negDiag.remove(r-c)
                curr[r][c] = "."
            
        backtrack(0)
        return res

        