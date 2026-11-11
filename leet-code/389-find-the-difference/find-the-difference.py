class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        sum = 0
        sum2 = 0
        for ch in s:
            sum += ord(ch)
        for ch in t:
            sum2+=ord(ch)
        
        return chr(sum2-sum)

       
            
            

        
        