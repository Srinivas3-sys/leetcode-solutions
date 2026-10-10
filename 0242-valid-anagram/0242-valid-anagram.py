#
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
#
# https://leetcode.com/problems/valid-anagram/
#

# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        list1="".join(sorted(s))
        list2="".join(sorted(t))
        if list1==list2:
            return True
        return False
        # @lc code=end
