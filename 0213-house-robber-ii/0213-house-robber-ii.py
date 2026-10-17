class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        def cases(nums):
            n = len(nums)-1
            if n == 0:
                return nums[0]
            prev2 = nums[0]
            prev = max(nums[0],nums[1])
            for i in range(2,n+1):
                take = nums[i] + prev2
                skip = prev
                curr = max(take,skip)
                prev2 = prev
                prev = curr
            return prev
        first = cases(nums[1:])
        last = cases(nums[:-1])
        return max(first,last)