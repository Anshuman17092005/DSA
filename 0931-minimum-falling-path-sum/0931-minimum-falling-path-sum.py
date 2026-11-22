class Solution(object):
    def minFallingPathSum(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        n = len(matrix)
        dp =  [[0]*n for _ in range(n)]
        for j in range(n):
            dp[n-1][j] = matrix[n-1][j]
        for i in range(n-2,-1,-1):
            for j in range(n):
                if j > 0:
                    down_left = dp[i+1][j-1]
                else:
                    down_left = float('inf')
                if j < n-1:
                    down_right = dp[i+1][j+1]
                else:
                    down_right = float('inf')
                down = dp[i+1][j]
                dp[i][j] = matrix[i][j] + min(down,down_left,down_right)
        return min(dp[0])