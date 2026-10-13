#
# @lc app=leetcode id=560 lang=python3
#
# [560] Subarray Sum Equals K
#
# https://leetcode.com/problems/subarray-sum-equals-k/
#

# @lc code=start
from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        pref=[]
        pref.append(0)
        n=len(nums)
        ans=0
        d=defaultdict(int)
        n=len(nums)
        for i in range(n):
            y=pref[i]+nums[i]
            pref.append(y)
        for i in range(n+1):
            x=pref[i]-k
            if x in d:
                ans+=d[x]
            d[pref[i]]+=1
        return ans



        
# @lc code=end
