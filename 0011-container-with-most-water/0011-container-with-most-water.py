class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        left = 0
        right = n - 1
        maxi = float('-inf')
        while left < right:
            area = (right-left)*min(height[left],height[right])
            maxi = max(maxi,area)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return maxi