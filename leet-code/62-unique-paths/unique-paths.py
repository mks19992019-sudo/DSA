class Solution:
    def uniquePaths(self, m, n) :
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        total = m + n - 2
        down = m - 1
        result = 1
        for i in range(1, down + 1):
            result = result * (total - i + 1) // i
        return result
        