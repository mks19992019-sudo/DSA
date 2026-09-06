class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        memo = {}

        def Tribonacci(n):
            if n == 0:
                return 0
            if n == 1:
                return 1
            if n == 2:
                return 1
            if n in memo:
                return memo[n]
            memo[n] = Tribonacci(n-1) + Tribonacci(n-2) + Tribonacci(n-3)

            return memo[n]
        return Tribonacci(n)
        