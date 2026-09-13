class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        maxi = float('-inf')
        l = 0
        r = n - 1
        while l < r:
            area = (r-l) * min(height[l],height[r])
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
            maxi = max(area,maxi)
        return maxi