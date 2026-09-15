class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        def firstFind(nums,target):
            left = 0
            right = len(nums)-1
            answer = -1
            while left <= right:
                mid = (left+right)//2
                if nums[mid] == target:
                    answer = mid
                    right = mid-1
                elif nums[mid] < target:
                    left = mid+1
                else:
                    right = mid-1
            return answer
        def lastFind(nums,target):
            left = 0
            right = len(nums)-1
            answer = -1
            while left <= right:
                mid = (left+right)//2
                if nums[mid] == target:
                    answer = mid
                    left = mid+1
                elif nums[mid] < target:
                    left = mid+1
                else:
                    right = mid-1
            return answer
        first = firstFind(nums,target)
        last = lastFind(nums,target)
        return [first,last]