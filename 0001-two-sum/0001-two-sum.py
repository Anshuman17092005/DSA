class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        freq = {}
        for i in range(len(nums)):
            needed = target - nums[i]
            if needed in freq:
                return [i,freq[needed]]
            freq[nums[i]] = freq.get(nums[i],i)