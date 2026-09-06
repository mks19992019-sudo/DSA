class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """

        memo = {}
        n = len(cost)

        def mincost(i):
            if i<=1:
                return cost[i]
            
            if i in memo:
                return memo[i]
            
            memo[i] = cost[i] + min(mincost(i-1),mincost(i-2))

            return memo[i]
        return min(mincost(n-1),mincost(n-2))

        