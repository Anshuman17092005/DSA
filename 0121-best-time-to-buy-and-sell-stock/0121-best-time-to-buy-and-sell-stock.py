class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        mini = prices[0]
        maxi = float('-inf')
        profit = 0
        for price in prices:
            if price < mini:
                mini = price
            profit = price - mini
            maxi = max(maxi,profit)
        return maxi
