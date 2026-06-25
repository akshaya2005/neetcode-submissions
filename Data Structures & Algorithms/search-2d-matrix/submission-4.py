class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        print(m, n)
        
        l = 0
        r = n # 4

        t = 0
        b = m # 3
       
        while l <= r and t <= b:
        
            col = (l + r) // 2
            row = (t + b) // 2
            
            if row >= m or col >= n:
                return False

            num = matrix[row][col]
            if num == target:
                return True
            if target < num:
                if target >= matrix[row][0]:
                    r = col - 1
                else:
                    b = row - 1
            else:
                if target <= matrix[row][-1]:
                    l = col + 1
                else:
                    t = row + 1
        return False

                