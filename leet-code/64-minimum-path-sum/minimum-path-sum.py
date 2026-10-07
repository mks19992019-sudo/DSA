class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        memo = {}
        raw = len(grid)
        col = len(grid[0])

        def dfs(i,j):
            
            if i >=raw or j>=col:
                return float('inf')
            
            if i == raw-1 and j == col-1:
                return grid[i][j]
            
            
            if (i,j) in memo:
                return memo[(i,j)]
            
            down = dfs(i+1,j)
            right=dfs(i,j+1)

            memo[(i,j)] = grid[i][j] + min(down,right)

            return memo[(i,j)]
        
        return dfs(0,0)

        
        