#
# @lc app=leetcode id=1137 lang=python3
#
# [1137] N-th Tribonacci Number
#
# https://leetcode.com/problems/n-th-tribonacci-number/
#

# @lc code=start
class Solution:
    def tribonacci(self, n: int) -> int:
        dp=[]
        dp.append(0)
        dp.append(1)
        dp.append(1)
        for i in range(3,n+1,1):
            y=dp[i-1]+dp[i-2]+dp[i-3]
            dp.append(y)
        return dp[n]
# @lc code=end
