#
# @lc app=leetcode id=424 lang=python3
#
# [424] Longest Repeating Character Replacement
#
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxf = res = 0
        count = collections.Counter()
        for i in range(len(s)):
            count[s[i]] += 1
            
            maxf = max(maxf, count[s[i]])
            if res < k + maxf:
                res += 1
            else:
                count[s[i - res]] -= 1
                
        return res

