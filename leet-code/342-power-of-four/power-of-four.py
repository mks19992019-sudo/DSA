class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n>0:
            if n==1:
                return True
            return (n & (n - 1)) == 0 and (n & 0x55555555) != 0
        else:
            return False
        




        