#
# @lc app=leetcode id=27 lang=python
#
# [27] Remove Element
#
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i, cur, end= 0,  0, len(nums)
        for i in range(end):
            if nums[i] != val:
                nums[cur] = nums[i]
                cur += 1
        return cur 
        

