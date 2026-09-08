class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        dp = [[-1] * (n+1) for _ in range(m+1)]
        dp[0][0] = grid[0][0]
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                up = float('inf')
                left = float('inf')
                if i > 0:
                    up = grid[i][j] + dp[i-1][j]
                if j > 0:
                    left = grid[i][j] + dp[i][j-1]
                dp[i][j] = min(up,left)
        return dp[m-1][n-1]