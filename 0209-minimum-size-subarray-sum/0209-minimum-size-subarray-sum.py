class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        mini = float('inf')
        total = 0
        for right in range(len(nums)):
            total += nums[right]
            while total >= target:
                mini = min(mini,right-left+1)
                total -= nums[left]
                left += 1
        if mini == float('inf'):
            return 0
        return mini