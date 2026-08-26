class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        curr = 0
        maxi = float('-inf')
        for right in range(len(nums)):
            curr = max(curr + nums[right],nums[right])
            maxi = max(curr,maxi)
        return maxi