class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        prev = 1
        prev2 = 1
        for i in range(2,n+1):
            curr = prev + prev2
            prev2 = prev
            prev = curr
        return prev
        
