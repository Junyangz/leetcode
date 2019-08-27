#
# @lc app=leetcode id=153 lang=python3
#
# [153] Find Minimum in Rotated Sorted Array
#
class Solution:
    def findMin(self, nums: List[int]) -> int:

        start, end = 0, len(nums) - 1
        if nums[start] < nums[end]: return nums[start]
        
        while start < end - 1:
            mid = (start + end) // 2
            if nums[mid] > nums[start]:
                start = mid
            else:
                end = mid

        return nums[end]
    
        # for i in range(1, len(nums)):
        #     if nums[i] < nums[i-1]:
        #         return nums[i]
        # return nums[0]

