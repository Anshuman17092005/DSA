class Solution:
  def canPartition(self,num):
    total = sum(num)
    if total % 2 != 0:
      return False
    target = total // 2
    dp = [[False] * (target + 1) for _ in range(len(num)+1)]
    def solve(arr,target,dp):
      n = len(arr)
      for i in range(n+1):
        dp[i][0] = True
      for i in range(n-1,-1,-1):
        for t in range(1,target + 1):
          take = False
          if arr[i] <= t:
            take = dp[i+1][t-arr[i]]
          notTake = dp[i+1][t]
          dp[i][t] = notTake or take
      return dp[0][target]
    return solve(num,target,dp)