#
# @lc app=leetcode id=56 lang=python3
#
# [56] Merge Intervals
#
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])

        merged = []
        for interval in intervals:
            # if the list of merged intervals is empty or if the current
            # interval does not overlap with the previous, simply append it.
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
            # otherwise, there is overlap, so we merge the current and previous
            # intervals.
                merged[-1][1] = max(merged[-1][1], interval[1])

        return merged
    
        # intervals = sorted(intervals)
        # for i in range(len(intervals) - 1):
        #     while i < len(intervals) - 1:
        #         if intervals[i][1] < intervals[i + 1][0]: break
        #         else:
        #             if intervals[i][1] >= intervals[i + 1][0] and intervals[i][1] <= intervals[i+1][1]:
        #                 intervals[i][1] = intervals[i+1][1]
        #                 intervals.pop(i + 1)
        #             else:
        #                 intervals.pop(i + 1)
        # return intervals

