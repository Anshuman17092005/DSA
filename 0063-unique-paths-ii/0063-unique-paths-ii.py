class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if obstacleGrid[0][0] == 1:
            return 0
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[0]*n for _ in range(m)]
        dp[0][0] = 1
        blocked = False

        for i in range(m):
            if obstacleGrid[i][0] == 1:
                blocked = True
            if not blocked:
                dp[i][0] = 1
        blocked = False
        for j in range(n):
            if obstacleGrid[0][j] == 1:
                blocked = True
            if not blocked:
                dp[0][j] = 1
        for i in range(1,m):
            for j in range(1,n):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[m-1][n-1]