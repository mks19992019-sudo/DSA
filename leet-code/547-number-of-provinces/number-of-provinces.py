class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """

        N = len(isConnected)
        visited = set()
        provinces = 0

        def DFS(city):
            visited.add(city)

            for nei in range(N):
                if isConnected[city][nei] == 1 and nei not in visited:
                    DFS(nei)
        
        for city in range(N):
            if city not in visited:
                provinces +=1
                DFS(city)

        return provinces

            
        
        