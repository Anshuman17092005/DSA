class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        jump = 0
        l = r = 0
        farthest = 0
        while(r < n-1):
            for i in range(l,r+1):
                farthest = max(farthest,i+nums[i])
            l = r+1
            r = farthest
            jump += 1
        return jump