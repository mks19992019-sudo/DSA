class Solution:
    def digitSum(self, s: str, k: int) -> str:
        
        def count(s):
            if len(s)<=k:
                return s
            ans_s =''
            for i in range(0,len(s),k):
                temp = 0
                for j in s[i:i+k]:
                    temp+= int(j)
                ans_s = ans_s + str(temp)
            return count(ans_s)
        return count(s)
                    


        