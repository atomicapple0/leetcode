class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        
        def helper(i,j):
            if i < 0 or i >= rows or j < 0 or j >= cols:
                return 0
            if grid[i][j] == '0':
                return 0
            grid[i][j] = '0'
            helper(i-1,j)
            helper(i+1,j)
            helper(i,j-1)
            helper(i,j+1)
            return 1

        count = 0
        for row in range(rows):
            for col in range(cols):
                count += helper(row,col)
        return count
            
        
        
        