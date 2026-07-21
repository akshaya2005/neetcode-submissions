class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False
    def add(self, word):
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.end = True
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for w in words:
            root.add(w)
        rows = len(board)
        cols = len(board[0])
        res = set()
        visited = set()
        def dfs(row, col, node, word):
            
            if row >= rows or col >= cols or row < 0 or col < 0 or (row, col) in visited or board[row][col] not in node.children:
                return

            word += (board[row][col])
            node = node.children[board[row][col]]
            visited.add((row,col))
            if node.end:
                res.add(word)
            
            for i, j in [(row+1, col), (row-1, col), (row, col+1), (row, col-1)]:
                dfs(i, j, node, word)
            
            visited.remove((row,col))
        
        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root, "")
        return list(res)
        


            
        
        