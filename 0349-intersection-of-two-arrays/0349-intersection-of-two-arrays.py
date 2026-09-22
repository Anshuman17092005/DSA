class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        result = []
        seen = set(nums2)
        for num in nums1:
            if num in seen and num not in result:
                result.append(num)
        return result