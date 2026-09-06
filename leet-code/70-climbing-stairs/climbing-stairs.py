class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        memo = {}
        def no_ways(n):

            if n == 1:
                return 1
            if n == 2:
                return 2
            if n in memo:
                return memo[n]
            memo[n] = no_ways(n-1) +  no_ways(n-2)

            return memo[n]
        
        return no_ways(n) 


        