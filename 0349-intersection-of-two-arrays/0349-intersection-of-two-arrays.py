class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        result = []
        nums1 = list(set(nums1))
        for num in nums1:
            if num in nums2:
                result.append(num)
        return result