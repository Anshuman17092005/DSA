class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        n = len(triangle)

        prev = triangle[n - 1][:]

        for i in range(n - 2, -1, -1):
            curr = [0] * len(triangle[i])

            for j in range(len(triangle[i])):
                curr[j] = triangle[i][j] + min(prev[j], prev[j + 1])

            prev = curr

        return prev[0]