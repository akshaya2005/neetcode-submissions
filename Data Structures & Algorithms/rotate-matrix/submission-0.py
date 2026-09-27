class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
    
        n = len(matrix)
        
        for i in range(n//2 + 1):
            for j in range(i, n-i-1):
                new_i, new_j = j, n-i-1
                curr = matrix[i][j]
                while True:
                    ## save whatever is at the new location
                    temp = matrix[new_i][new_j]
                    ## move curr to the new location
                    matrix[new_i][new_j] = curr
                    ## if the new location is (i,j)
                    ## you've made a full circle so break
                    if new_i == i and new_j == j:
                        break
                    ## rotation coordinates
                    new_i, new_j = new_j, n-new_i-1
                    ## rotate the thing that was at the new location
                    curr = temp



        



        
        