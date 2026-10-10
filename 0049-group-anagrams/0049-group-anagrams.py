#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#
# https://leetcode.com/problems/group-anagrams/
#

# @lc code=start
from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        s=defaultdict(list)
        for x in strs:
            y="".join(sorted(x))
            s[y].append(x)
        ans=[]
        for x in s:
            ans.append(s[x])
        return ans

            
# @lc code=end
