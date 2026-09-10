class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        pos = 0
        neg = 1
        n = len(nums)
        result = [0] * n
        for num in nums:
            if num> 0:
                result[pos] = num
                pos += 2
            else:
                result[neg] = num
                neg += 2
        return result