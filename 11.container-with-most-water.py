#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#
class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        Two pointers scanning
        starting from two ends since x-coordinate is maximized
        Different from 041 Trapping Rain Water, since here it only considers two lines
        :param height: array
        :return: max area, integer
        """
        start = 0
        end = len(height)-1

        max_area = -1 << 32
        while start < end:
            area = min(height[start], height[end])*(end-start)
            max_area = max(area, max_area)

            # move the shorter boarder
            # move two pointers
            if height[start] < height[end]:
                start += 1
            else:
                end -= 1

        return max_area
