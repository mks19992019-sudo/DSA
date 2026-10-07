from collections import deque
class Solution(object):
    def updateMatrix(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """
        m = len(mat)
        n = len(mat[0])

        q = deque()
        visited = set()
        
        direction = [
            (-1,0),#up
            (0,-1),#left
            (0,1),#right
            (1,0)#down
        ]

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    q.append((i,j))
                    visited.add((i,j))
        
        while q:
            raw , col = q.popleft()
            for raw_ , col_ in direction:
                new_raw = raw + raw_
                new_col = col + col_

                if (0<= new_raw<m) and (0<=new_col<n) and (new_raw ,new_col) not in visited:
                    mat[new_raw][new_col] = mat[raw][col] + 1
                    q.append((new_raw,new_col))
                    visited.add((new_raw,new_col))
        return mat


        


       

        

        