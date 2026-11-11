class Solution(object):
    def countServers(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        n = len(grid)
        m = len(grid[0])

        row_count = [0]*n
        col_count = [0]*m

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    row_count[i] +=1
                    col_count[j] +=1
        total_communicate = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j]:
                    if row_count[i] >1 or col_count[j]>1:
                        total_communicate +=1
        return total_communicate


        