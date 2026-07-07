class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
    
        rows = len(board)
        cols = len(board[0])
        curr = []
        visited = set()
        def helper(row, col, length):
        
            if len(curr) == len(word):
                return True
           
            if (row < 0 or col < 0 or row >= rows or col >= cols or word[length] != board[row][col] or (row, col) in visited) :
                return False    
            curr.append(board[i][j])
            visited.add((row, col))
            wordExists = helper(row+1, col, length + 1) or helper(row-1, col, length + 1) or helper(row, col-1, length + 1) or helper(row, col+1, length + 1)
            visited.remove((row, col))
            curr.pop()
            return wordExists
      
            
        
        for i in range(rows):
            for j in range(cols):
                if helper(i, j, 0): return True
        return False

