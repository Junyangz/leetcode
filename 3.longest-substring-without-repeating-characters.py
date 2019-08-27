#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        buffer = {}
        start = maxlength = 0

        for i in range(len(s)):
            start = max(buffer.get(s[i], 0), start)
            maxlength = max(maxlength, i - start + 1)
            buffer[s[i]] = i + 1

        return maxlength

