from collections import deque
class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])
        q = deque()
        visited = set()

        for j in range(n):
            if board[0][j] == 'O' and ((0,j) not in visited):
                q.append((0,j))
                visited.add((0,j))
            
            if board[m-1][j] == 'O' and (m-1,j) not in visited:
                q.append((m-1,j))
                visited.add((m-1,j))
        for i in range(m):
            if board[i][0] == "O" and (i, 0) not in visited:
                visited.add((i, 0))
                q.append((i, 0))

            if board[i][n-1] == "O" and (i, n-1) not in visited:
                visited.add((i, n-1))
                q.append((i, n-1))
        directions = [
            (-1,0),#up
            (1,0),#down
            (0,-1),#left
            (0,1)#right
        ]

        while q:
            r , c = q.popleft()

            for r_ , c_ in directions:
                nr = r + r_
                nc = c + c_

                if 0<=nr<m and 0<=nc<n and board[nr][nc]=="O" and (nr,nc) not in visited:
                    q.append((nr,nc))
                    visited.add((nr,nc))
        
        for i in range(m):
            for j in range(n):
                if board[i][j]=="O" and (i,j) not in visited:
                    board[i][j] = "X"
        return board


        
        


        