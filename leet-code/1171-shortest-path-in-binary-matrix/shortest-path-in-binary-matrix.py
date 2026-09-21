class Solution(object):
    def shortestPathBinaryMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        

        directions = [
            (-1,0),#up
            (1,0),#down
            (0,-1),#left
            (0,1),#right
            (1,1),
            (-1,-1),
            (1,-1),
            (-1,1)
        ]
        m = len(grid)
        n = len(grid[0])
        if grid[0][0] == 1 or grid[m-1][n-1] == 1:
            return -1
        visited = set()

        q = deque()
        q.append((0,0))
        visited.add((0,0))
        distance = 1

        while q:
            for i in range(len(q)):
                raw , col = q.popleft()
                if raw == m-1 and col == n-1:
                    return distance 
                for raw_ , col_ in directions:
                    new_raw  = raw + raw_
                    new_col = col + col_
                    if (0<=new_raw<m and 0<=new_col<n and grid[new_raw][new_col]==0 and (new_raw,new_col) not in visited):
                        
                        q.append((new_raw,new_col))
                        visited.add((new_raw,new_col))

            distance +=1

        return -1
                    






        

        