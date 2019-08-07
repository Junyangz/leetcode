#
# @lc app=leetcode id=300 lang=python3
#
# [300] Longest Increasing Subsequence
#
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # tails = [0] * len(nums)
        # size = 0
        # for x in nums:
        #     i, j = 0, size
        #     while i != j:
        #         m = (i + j) // 2
        #         if tails[m] < x:
        #             i = m + 1
        #         else:
        #             j = m
        #     tails[i] = x
        #     size = max(i + 1, size)
        # return size
        dp=[ [0, math.inf] ] + [ [1, n] for n in nums ]
        
        for i, n in enumerate(nums, start=1):
            ml = 1
            for j in reversed(range(i)):
                if n > dp[j][1]:
                    ml = max(ml, dp[j][0] + 1)
            dp[i][0] = ml

        return max(dp[i][0] for i in range(len(nums) + 1))
