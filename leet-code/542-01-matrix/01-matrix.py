from collections import deque
class Solution(object):
    def updateMatrix(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """
        grid = mat

        directions = [
            (-1,0),#up
            (1,0),#down
            (0,-1),#left
            (0,1)#right 
        ]

        visited = set()
        q = deque()

        m = len(grid)
        n = len(grid[0])

        for i in range(m):
            for j in range(n):
                if grid[i][j]==0:
                    q.append((i,j))
                    visited.add((i,j))
        
        while q:
            raw , col = q.popleft()
            for raw_ , col_ in directions:
                nr = raw+raw_
                nc = col + col_

                if 0<=nr<m and 0<=nc<n and (nr,nc) not in visited:
                    grid[nr][nc] = grid[raw][col] + 1
                    q.append((nr,nc))
                    visited.add((nr,nc))
        return grid

        

        