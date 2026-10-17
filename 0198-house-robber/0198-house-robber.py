class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)-1
        if n == 0:
            return nums[0]
        prev2 = nums[0]
        if n >= 1:
            prev = max(nums[0],nums[1])
        for i in range(2,n+1):
            take = nums[i] + prev2
            skip = prev
            curr = max(take,skip)
            prev2 = prev
            prev = curr
        return prev