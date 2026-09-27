from collections import deque
class Solution(object):
    def closedIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])

        visited = set()
        directions =[
            (-1,0),#up
            (1,0),#down
            (0,-1),#left
            (0,1)#right 

        ]
        ans=0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0 and (i,j) not in visited:
                    close = True
                    q = deque()
                    q.append((i,j))
                    visited.add((i,j))

                    while q:
                        r , c = q.popleft()
                        if r == 0 or r ==m-1 or c==0 or c ==n-1:
                            close = False

                        for r_,c_ in directions:
                            nr = r+r_
                            nc = c+c_

                            if 0<=nr<m and 0<=nc<n and grid[nr][nc] == 0 and (nr,nc) not in visited:
                                q.append((nr,nc))
                                visited.add((nr,nc))
                    
                    if close:
                        ans +=1
        return ans

                        



        
        