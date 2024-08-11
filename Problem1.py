## Problem1 
#Custom Sort String (https://leetcode.com/problems/custom-sort-string/)
class Solution:
    def customSortString(self, order, s):
        s_dict = {}
        res = ""
        for ch in s:
            s_dict[ch] = s_dict.get(ch,0) + 1

        for ch in order:
            if ch in s_dict:
                count = s_dict[ch]
                res += ch * count
                del s_dict[ch]

        # Append remaining characters not in order
        for ch in s_dict:
            res += ch * s_dict[ch]

        return res


order = "cba"
s = "abcd"
sol = Solution()
print(sol.customSortString(order, s))