class Solution:
    def findTheDifference(self, s: str, t: str) -> str:

        dist = {}

        for ch in s:
            dist[ch] = dist.get(ch,0) + 1
        
        for ch in t:
            if dist.get(ch,0) == 0:
                return ch
            dist[ch] -=1

            
            

        
        