from collections import deque
class Solution(object):
    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """ 
        m = len(image)
        n = len(image[0])
        direction =[
            (-1,0),
            (0,-1),
            (0,1),
            (1,0)
        ]

        current_color = image[sr][sc]

        if current_color == color:
            return image

        q = deque()
        #visited = set()

        q.append((sr,sc))
        #visited.add((sr,sc))
        image[sr][sc] = color

        while q:
            raw , col = q.popleft()


            for r_ , c_ in direction:
                nr = raw+r_
                nc = col+c_

                if (0<=nr<m) and (0<=nc<n) and image[nr][nc]==current_color: #and (nr,nc) not in #visited:
                    image[nr][nc] = color
                    q.append((nr,nc))
                    #visited.add((nr,nc))
        return image









        