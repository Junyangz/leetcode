#
# @lc app=leetcode id=435 lang=python3
#
# [435] Non-overlapping Intervals
#
# https://leetcode.com/problems/non-overlapping-intervals/description/
#
# algorithms
# Medium (41.83%)
# Likes:    571
# Dislikes: 25
# Total Accepted:    46K
# Total Submissions: 109.8K
# Testcase Example:  '[[1,2]]'
#
# Given a collection of intervals, find the minimum number of intervals you
# need to remove to make the rest of the intervals non-overlapping.
# 
# 
# 
# 
# 
# 
# Example 1:
# 
# 
# Input: [[1,2],[2,3],[3,4],[1,3]]
# Output: 1
# Explanation: [1,3] can be removed and the rest of intervals are
# non-overlapping.
# 
# 
# Example 2:
# 
# 
# Input: [[1,2],[1,2],[1,2]]
# Output: 2
# Explanation: You need to remove two [1,2] to make the rest of intervals
# non-overlapping.
# 
# 
# Example 3:
# 
# 
# Input: [[1,2],[2,3]]
# Output: 0
# Explanation: You don't need to remove any of the intervals since they're
# already non-overlapping.
# 
# 
# 
# 
# Note:
# 
# 
# You may assume the interval's end point is always bigger than its start
# point.
# Intervals like [1,2] and [2,3] have borders "touching" but they don't overlap
# each other.
# 
# 
#
class Solution:
    def eraseOverlapIntervals(self, I: List[List[int]]) -> int:
        if not I: return 0
        I.sort(key = lambda x: x[0])

        currEnd, cnt = I[0][1], 0

        for i in I[1:]:
            if currEnd > i[0]:
                cnt += 1
                currEnd = min(i[1], currEnd)
            else:
                currEnd = i[1]

        return cnt
        

