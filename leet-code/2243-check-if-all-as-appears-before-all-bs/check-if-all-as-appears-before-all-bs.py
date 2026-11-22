class Solution:
    def checkString(self, s: str) -> bool:
        b = 0
        count = 0

        for ch in s:
            if ch =='b':
                count +=1
            if ch =='a' and count >0:
                return False
        
        return True
        