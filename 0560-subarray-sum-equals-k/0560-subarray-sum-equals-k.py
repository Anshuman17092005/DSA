class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count = 0
        freq = {0:1}
        curr = 0
        prev = 0
        for num in nums:
            curr += num
            prev = curr - k
            if prev in freq:
                count += freq[prev]
            freq[curr] = freq.get(curr,0)+1
        return count