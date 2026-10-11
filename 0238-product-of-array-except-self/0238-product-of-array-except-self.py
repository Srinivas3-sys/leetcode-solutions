#
# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
#
# https://leetcode.com/problems/product-of-array-except-self/
#

# @lc code=start
class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        pref=[]
        pref.append(1)
        suff=[]
        suff.append(1)
        suff.append(1)
        n=len(nums)
        for i,x in enumerate(nums):
            y=pref[i]*x
            pref.append(y)
            z=suff[i+1]*nums[n-i-1]
            suff.append(z)
        suff.pop()
        suff.reverse()
        ans=[]
        for i in range(n):
            k=pref[i]*suff[i]
            ans.append(k)
        return ans

        


            
# @lc code=end
