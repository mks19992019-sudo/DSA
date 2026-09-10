from collections import deque
class Solution(object):
    def validPath(self, n, edges, source, destination):
        """
        :type n: int
        :type edges: List[List[int]]
        :type source: int
        :type destination: int
        :rtype: bool
        """

        graph = {}
        for u ,v in edges:
            if u not in graph:
                graph[u] = []

            if v not in graph:
                graph[v] = []

            graph[u].append(v)
            graph[v].append(u)
        
        visted =set()
        queue = deque()
        queue.append(source)
        visted.add(source)

        while queue:
            node = queue.popleft()

            if node == destination:
                return True
            
            for neaber in graph[node]:
                if neaber not in visted:
                    visted.add(neaber)
                    queue.append(neaber)
        return False

        

        


        


        