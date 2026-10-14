class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """

        n = len(word1)
        m = len(word2)
        
        dp = [[0]*(n+1) for i in range(m+1)]

        for i in range(m+1):
            for j in range(n+1):
                if  i>0 and j>0 and word1[j-1]==word2[i-1] :
                    dp[i][j] = dp[i-1][j-1]
                else:

                    if i==0 and j>0:
                        dp[i][j]= dp[i][j-1] +1
                    elif j==0 and i>0:
                        dp[i][j] = dp[i-1][j] + 1
                    elif i>0 and j>0:
                        dp[i][j] = min(dp[i-1][j]+1,dp[i][j-1]+1,dp[i-1][j-1]+1)
        return dp[m][n]


        
        