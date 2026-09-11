class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        seen = set(nums)
        for num in seen:
            if num-1 not in seen:
                current = num
                length = 0
                while current in seen:
                    current += 1
                    length += 1
                count = max(count,length)
        return count