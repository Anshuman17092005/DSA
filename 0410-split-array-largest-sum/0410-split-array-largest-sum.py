class Solution(object):
    def splitArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        low = max(nums)
        high = sum(nums)
        while low <= high:
            mid = (low + high) // 2
            subarray = 1
            curr = 0
            for num in nums:
                if curr+num <= mid:
                    curr += num
                else:
                    subarray += 1
                    curr = num
            if subarray > k:
                low = mid+1
            else:
                high = mid-1
        return low