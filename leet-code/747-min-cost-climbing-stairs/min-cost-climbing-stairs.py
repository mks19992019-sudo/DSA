class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        n = len(cost)
        dp= [0]*(n+2)

        for i in range(n-1,-1,-1):
            dp[i] = cost[i]+min(dp[i+1],dp[i+2])

        return min(dp[0],dp[1])

        

        