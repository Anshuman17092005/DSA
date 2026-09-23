class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        def firstFind(nums,target):
            low = 0
            high = len(nums)-1
            answer = -1
            while low <= high:
                mid = (low + high) // 2
                if nums[mid] == target:
                    answer = mid
                    high = mid-1
                elif nums[mid] < target:
                    low = mid+1
                else:
                    high = mid-1
            return answer
        def lastFind(nums,target):
            low = 0
            high = len(nums)-1
            answer = -1
            while low<=high:
                mid = (low+high)//2
                if nums[mid] == target:
                    answer = mid
                    low = mid+1
                elif nums[mid] < target:
                    low = mid+1
                else:
                    high = mid-1
            return answer
        first = firstFind(nums,target)
        last = lastFind(nums,target)
        return [first,last]