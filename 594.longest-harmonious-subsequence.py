#
# @lc app=leetcode id=594 lang=python3
#
# [594] Longest Harmonious Subsequence
#
class Solution:
    def findLHS(self, nums: List[int]) -> int:
        if not nums: return 0
        c = collections.Counter(nums)
        return max([max(c.get(n - 1, 0), c.get(n + 1, 0)) + c.get(n) 
                    if max(c.get(n - 1, 0), c.get(n + 1, 0)) > 0 else 0
                   for n in c.keys()])

