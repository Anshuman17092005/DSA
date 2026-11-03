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
        dp = [[-1]*n for _ in range(m)]
        def solve(i,j,dp):
            if i < 0 or j < 0:
                return 0
            if obstacleGrid[i][j] == 1:
                return 0
            if i == 0 and j == 0:
                return 1
            if dp[i][j] != -1:
                return dp[i][j]
            above = solve(i-1,j,dp)
            left = solve(i,j-1,dp)
            dp[i][j] = above+left
            return dp[i][j]
        return solve(m-1,n-1,dp)