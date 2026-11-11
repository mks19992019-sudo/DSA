class Solution:
    def countBits(self, n: int) -> list[int]:
        if n ==0:
            return [0]
        
        DP = [0]*(n+1)
        
        temp = 2
        DP[0]=0
        DP[1]=1

        for i in range(2,1+n):

            if temp == i:
                prev_2_place = i
                DP[i] = 1
                temp = temp*2
            else:
                DP[i] = DP[i-prev_2_place] +1

        return DP
        



        
        
        