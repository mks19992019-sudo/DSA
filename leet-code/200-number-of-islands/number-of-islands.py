from collections import deque
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        visited = set()
        count = 0

        directions = [
            (-1,0),#up
            (0,-1),#left
            (0,1),#right
            (1,0)#down
        ]

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1' and (i,j) not in visited:
                    count +=1
                    q = deque()
                    q.append((i,j))

                    visited.add((i,j))

                    while q:
                        raw_ , col_ = q.popleft()


                        for dr ,  dc in directions:
                            new_raw = raw_ + dr
                            new_col = col_ + dc

                            if (0<= new_raw < m) and (0<=new_col<n)and grid[new_raw][new_col]=='1'and (new_raw,new_col) not in visited :
                                visited.add((new_raw, new_col))
                                q.append((new_raw, new_col))
        return count





        