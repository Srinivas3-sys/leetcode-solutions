#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#
# https://leetcode.com/problems/longest-substring-without-repeating-characters/
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n=len(s)
        freq=[0]*128
        left=0
        ans=0
        for right in range(1,n+1,1):
            if freq[ord(s[right-1])-ord('a')]>=left:
                left=freq[ord(s[right-1])-ord('a')]+1
            freq[ord(s[right-1])-ord('a')]=right
            ans=max(ans,right-left+1)
        return ans
                

# @lc code=end