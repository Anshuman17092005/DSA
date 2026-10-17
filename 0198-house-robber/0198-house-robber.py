class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)-1
        dp = [-1] * (n+1)
        dp[0] = nums[0]
        if n >= 1:
            dp[1] = max(nums[0],nums[1])
        for i in range(2,n+1):
            take = nums[i] + dp[i-2]
            skip = dp[i-1]
            dp[i] = max(take,skip)
        return dp[n]