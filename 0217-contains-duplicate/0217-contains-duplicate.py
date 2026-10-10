#
# @lc app=leetcode id=217 lang=python3
#
# [217] Contains Duplicate
#
# https://leetcode.com/problems/contains-duplicate/
#

# @lc code=start
class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        map={}
        n=len(nums)
        for i,x in enumerate(nums):
            if x in map:
                return True
            else:
                map[x]=i
        return False
# @lc code=end
