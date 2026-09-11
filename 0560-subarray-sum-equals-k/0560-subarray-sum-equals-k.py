class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        current_sum = 0
        previous_sum = 0
        count = 0
        freq = {0:1}
        for num in nums:
            current_sum += num
            needed = current_sum-k
            if needed in freq:
                count += freq[needed]
            freq[current_sum] = freq.get(current_sum,0)+1
        return count