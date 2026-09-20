from collections import deque
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """

        m = len(grid)
        n = len(grid[0])
        Visited = set()
        No_Islands =0
        directions = [
            (-1,0),#up
            (0,-1),#left
            (1,0),#down
            (0,1)#right
        ]

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1' and (i,j) not in Visited:
                    No_Islands +=1
                    q = deque()
                    q.append((i,j))
                    Visited.add((i,j))

                    while q:
                        raw, col = q.popleft()

                        for raw_ , col_ in directions:

                            new_raw = raw + raw_ 
                            new_col = col + col_

                            if (0<= new_raw < m) and (0<=new_col<n) and grid[new_raw][new_col] =="1" and (new_raw,new_col) not in Visited:
                                q.append((new_raw,new_col))
                                Visited.add((new_raw,new_col))
        return No_Islands





        