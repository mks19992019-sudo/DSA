class Solution:
    def countBits(self, n: int) -> list[int]:
        DP = [0]*(n+1)
        temp = 2

        for i in range(n+1):
            count = 0
            if i % 2 !=0:
                DP[i] = DP[i-1]+1
                continue
            if temp ==i:
                DP[i] = 1
                temp = temp *2
                continue

            num =i
            while num >0:
                count += num&1
                num = num>>1
            DP[i] = count
        return DP
        
        