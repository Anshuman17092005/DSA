class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total = 0
        maxSum = float('-inf')
        for num in nums:
            total += num
            maxSum = max(maxSum,total)
            if total < 0:
                total = 0
        return maxSum