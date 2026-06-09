class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        
        def dfs(r,c,length):
            if length == len(word):
                return True
            if (r < 0 or c < 0 or r >= rows or c >= cols or word[length] != board[r][c] or board[r][c] == '#'):
                return False

            
            board[r][c] = '#'
            res = (dfs(r + 1, c, length + 1) or 
                   dfs(r, c + 1, length + 1) or 
                   dfs(r - 1, c, length + 1) or 
                   dfs(r, c - 1, length + 1))
            board[r][c] = word[length]
            return res

        for i in range(rows):
            for j in range(cols):
                if dfs(i,j, 0): return True
        return False

        