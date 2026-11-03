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
        prev = [0] * n
        for i in range(m):
            curr = [0] * n
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    curr[j] = 0
                elif i == 0 and j == 0:
                    curr[j] = 1
                else:
                    curr[j] = prev[j] + curr[j-1]
            prev = curr
        return prev[n-1]