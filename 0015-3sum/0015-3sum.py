#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#
# https://leetcode.com/problems/3sum/
#

# @lc code=start
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
      nums.sort()
      s=set()
      n=len(nums)
      for left1 in range(n-2):
        left2=left1+1
        right=n-1
        while left2<right:
            x=nums[left2]
            y=nums[right]
            target=-nums[left1]
            if x+y<target:
                left2+=1
            elif x+y>target:
                right-=1
            elif x+y==target:
                temp=(nums[left1],x,y)
                s.add(temp)
                left2+=1
                right-=1
        
      ans=[list(t) for t in s]
      return ans 


# @lc code=end
