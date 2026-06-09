class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board)
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [[set() for _ in range(3)] for _ in range(3)] 

        for i in range(n):
            for j in range(n):
                if board[i][j] == ".":
                    continue
                num = board[i][j]
                b1, b2 = i // 3, j // 3
                if num in rows[i] or num in cols[j] or num in boxes[b1][b2]:
                    return False
                rows[i].add(num)
                cols[j].add(num)
                boxes[b1][b2].add(num)
                print(boxes)
        return True
