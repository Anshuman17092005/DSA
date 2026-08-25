class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        prev = [0] * n
        prev[0] = 1
        for i in range(m):
            curr = [0] * n
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    curr[j] = 0
                elif i == 0 and j == 0:
                    curr[j] = 1
                else:
                    up = prev[j]
                    left = curr[j-1] if j > 0 else 0
                    curr[j] = up + left
            prev = curr
        return prev[n-1]