class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        prev = [1] * n
        for i in range(1,m):
            curr = [1]*n
            for j in range(1,n):
                curr[j] = prev[j] + curr[j-1]
            prev = curr
        
        return prev[n-1]