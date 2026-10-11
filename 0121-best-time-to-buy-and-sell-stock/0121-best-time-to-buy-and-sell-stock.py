#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        pref=[]
        n=len(prices)
        for i,x in enumerate(prices):
            if i==0:
                pref.append(prices[0])
            else:
                y=min(pref[i-1],prices[i])
                pref.append(y)
        ans=0
        for i in range(n):
            ans=max(ans,prices[i]-pref[i])
        return ans
            

# @lc code=end
