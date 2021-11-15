class Solution:
    def maximalSquare(self, matrix) -> int:
        rows = len(matrix)
        cols = len(matrix[0])
        
        for i in range(rows):
            for j in range(cols):
                matrix[i][j] = int(matrix[i][j])
        
        for idx in range((rows+cols) // 2):
            # go right, from min(i,cols) to cols
            i = min(idx,rows-1)
            for r in range(min(i,cols), cols):
                if i-1 >= 0 and r-1 >= 0 and matrix[i][r] == 1:
                    score = min(matrix[i-1][r], matrix[i][r-1], matrix[i-1][r-1])
                    matrix[i][r] = 1 if score == 0 else score + 1
            i = min(idx,cols-1)
            # go down, from min(i+1,rows) to rows
            for d in range(min(i+1,rows), rows):
                if i-1 >= 0 and d-1 >= 0 and matrix[d][i] == 1:
                    score = min(matrix[d-1][i], matrix[d][i-1], matrix[d-1][i-1])
                    matrix[d][i] = 1 if score == 0 else score + 1
        
        sol = 0
        for i in range(rows):
            for j in range(cols):
                sol = max(sol, matrix[i][j])
        return sol * sol