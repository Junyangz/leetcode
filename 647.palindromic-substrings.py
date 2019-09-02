#
# @lc app=leetcode id=647 lang=python3
#
# [647] Palindromic Substrings
#
# https://leetcode.com/problems/palindromic-substrings/description/
#
# algorithms
# Medium (57.65%)
# Likes:    1589
# Dislikes: 82
# Total Accepted:    115.3K
# Total Submissions: 199.7K
# Testcase Example:  '"abc"'
#
# Given a string, your task is to count how many palindromic substrings in this
# string.
# 
# The substrings with different start indexes or end indexes are counted as
# different substrings even they consist of same characters.
# 
# Example 1:
# 
# 
# Input: "abc"
# Output: 3
# Explanation: Three palindromic strings: "a", "b", "c".
# 
# 
# 
# 
# Example 2:
# 
# 
# Input: "aaa"
# Output: 6
# Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
# 
# 
# 
# 
# Note:
# 
# 
# The input string length won't exceed 1000.
# 
# 
# 
# 
#
class Solution:
    def countSubstrings(self, s: str) -> int:
        N = len(s)
        ret = 0
        for i in range(2 * N - 1):
            left = i // 2
            right = left + i % 2
            while left >= 0 and right < N and s[left] == s[right]:
                ret += 1
                left -= 1
                right += 1
        return ret

        

