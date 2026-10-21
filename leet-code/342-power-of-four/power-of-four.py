class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n<=0:
            return False

        if n == 1:
            return True
        return (n & (n-1) ==0) and (n & 0x5555555555 != 0)




        