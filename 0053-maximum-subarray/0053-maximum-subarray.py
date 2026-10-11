#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#
# https://leetcode.com/problems/maximum-subarray/
#

# @lc code=start
class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        ans=-1e9
        sum=-1e9
        for x in nums:
            sum=max(x,sum+x)
            ans=max(ans,sum)
        return ans
# @lc code=end
