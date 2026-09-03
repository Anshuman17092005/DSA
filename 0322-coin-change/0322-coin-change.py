class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp = [-1] * (amount + 1)
        def solve(amount,dp):
            mini = float('inf')
            if amount == 0:
                return 0
            if amount < 0:
                return float('inf')
            if dp[amount] != -1:
                return dp[amount]
            for coin in coins:
                mini = min(mini , 1+solve(amount - coin,dp))
            dp[amount] = mini
            return dp[amount]
        ans = solve(amount,dp)
        if ans == float('inf'):
            return -1
        return ans