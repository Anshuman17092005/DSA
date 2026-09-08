class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 1:
            return nums[0]
        dp = [-1]*(n)
        dp[0] = nums[0]
        dp[1] = max(nums[0],nums[1])
        for i in range(2,n):
            take = nums[i] + dp[i-2]
            notTake = dp[i-1]
            dp[i] = max(take,notTake)
        return dp[n-1]