class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        rev_s = s[::-1]
        n = len(s)

        dp = [[0]*(n+1) for i in range(n+1)]

        for i in range(1,n+1):
            for j in range(1,n+1):
                if s[j-1] == rev_s[i-1]:
                    dp[i][j] = dp[i-1][j-1]+1
                else:
                    dp[i][j] = max(dp[i-1][j],dp[i][j-1])
        return dp[n][n]
        