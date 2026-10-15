#
# @lc app=leetcode id=746 lang=python3
#
# [746] Min Cost Climbing Stairs
#
# https://leetcode.com/problems/min-cost-climbing-stairs/
#

# @lc code=start
class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        n=len(cost)
        dp=[]
        dp.append(0)
        dp.append(0)
        for i in range(2,n+1,1):
            y=min(dp[i-1]+cost[i-1],dp[i-2]+cost[i-2])
            dp.append(y)
        return dp[n]

# @lc code=end
