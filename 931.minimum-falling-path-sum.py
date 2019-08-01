# half understand ,review need at least once.
# dp solution
#
# @lc app=leetcode id=931 lang=python3
#
# [931] Minimum Falling Path Sum
#
class Solution:
    def minFallingPathSum(self, A: List[List[int]]) -> int:
        N = len(A)

        while len(A) >= 2:
            row = A.pop()
            for i in range(N):
                A[-1][i] += min(row[max(0, i - 1): min(i + 1, N - 1) + 1])
        
        return min(A[0])
        

