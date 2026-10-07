class Solution(object):
    def shortestPathBinaryMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        if grid[0][0] == 1 or grid[m-1][n-1]:
            return -1

        directions =[
            (-1,0),#up
            (0,-1),# left
            (0,1),#right
            (1,0),#down
            (-1,-1),
            (1,1),
            (1,-1),
            (-1,1)
        ]

        q = deque()
        visited = set()
        q.append((0,0))
        visited.add((0,0))
        distance = 1

        while q:
            for i in range(len(q)):
                raw , col = q.popleft()

                if raw == m-1 and col == n-1:
                    return distance

                for raw_ , col_ in directions:
                    nr = raw+raw_
                    nc =col+col_

                    if (0<=nr<m) and (0<=nc<n) and (nr,nc) not in visited and grid[nr][nc]==0:
                        q.append((nr,nc))
                        visited.add((nr,nc))
            distance +=1
        return -1


                    


        

       
                    






        

        