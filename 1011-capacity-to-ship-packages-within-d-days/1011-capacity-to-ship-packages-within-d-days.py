class Solution(object):
    def shipWithinDays(self, weights, days):
        """
        :type weights: List[int]
        :type days: int
        :rtype: int
        """
        low = max(weights)
        high = sum(weights)
        while low <= high:
            mid = (low+high)//2
            days_needed = 1
            curr = 0
            for weight in weights:
                if curr+weight <= mid:
                    curr += weight
                else:
                    days_needed += 1
                    curr = weight
            if days_needed <= days:
                high = mid-1
            else:
                low = mid+1
        return low          