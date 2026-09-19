from collections import deque

class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        q = deque()
        fresh = 0

        m = len(grid)
        n = len(grid[0])


        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    q.append((i,j))
                elif grid[i][j] ==1:
                    fresh +=1
        
        directions =[
            (-1,0),#up
            (0,-1), #left
            (0,1),# right
            (1,0) # down

        ]
        min = 0

        while q and fresh >0:
            for i in range(len(q)):
                raw , col = q.popleft()
                for raw_ , col_ in directions:
                    new_raw = raw + raw_
                    new_col = col + col_
                    if (0<=new_raw<m) and (0<=new_col<n) and (grid[new_raw][new_col] == 1):
                        grid[new_raw][new_col] = 2
                        fresh -=1
                        q.append((new_raw,new_col))

            min +=1
        if fresh > 0:
            return -1
        
        return min



            

        