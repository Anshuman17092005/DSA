class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        maxi = 0
        mini = float('inf')
        for i in prices:
            if i < mini:
                mini = i
            profit = i - mini
            maxi = max(profit,maxi)
        return maxi