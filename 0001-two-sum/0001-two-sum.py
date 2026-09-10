class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        freq = {}
        for i in range(len(nums)):
            x = target - nums[i]
            if x in freq:
                return [freq[x],i]
            freq[nums[i]] = i