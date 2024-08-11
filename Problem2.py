
## Problem2 

#Longest Substring Without Repeating Characters(https://leetcode.com/problems/longest-substring-without-repeating-characters/)
class Solution:
    def lengthOfLongestSubstring(self,s):
        l = 0
        res = 0
        s_set = set()
        for r in range(len(s)):
            if s[r] in s_set:
                s_set.remove(s[l])
                l = l+1

            s_set.add(s[r])
            res = max(res, r-l+1)

        return res

s = "abcabcbb"
sol = Solution()
print(sol.lengthOfLongestSubstring(s))


