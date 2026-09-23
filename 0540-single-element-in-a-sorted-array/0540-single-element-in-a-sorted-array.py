class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        low = 0
        high = len(nums)-1
        while low < high:
            mid = (low+high)//2
            if mid % 2 != 0:
                mid = mid-1
            if nums[mid] == nums[mid+1]:
                low = mid+2
            else:
                high = mid
        return nums[low]