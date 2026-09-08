class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        n = len(triangle)
        dp = [[0] * len(row) for row in triangle]
        for i in range(n):
            dp[n-1][i] = triangle[n-1][i]
        for i in range(n-2,-1,-1):
            for j in range(len(triangle[i])):
                d = dp[i+1][j]
                dg = dp[i+1][j+1]
                dp[i][j] = triangle[i][j] + min(d,dg)
        return dp[0][0]