class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # if not nums:
        #     return 0
        if len(nums) == 1:
            return nums[0]
        def case(arr):
            n = len(arr)
            prev2 = 0
            prev = 0
            for money in arr:
                curr = max(prev,money+prev2)
                prev2 = prev
                prev = curr
            return prev
        case1 = case(nums[:-1])
        case2 = case(nums[1:])
        return max(case1,case2)
