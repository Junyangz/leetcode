# ~review required~
# review done AT 2019-07-31 22:34:56
# dp solution

# Alex and Lee continue their games with piles of stones.  There are a number of piles arranged in a row, and each pile has a positive integer number of stones piles[i].  The objective of the game is to end with the most stones. 
# Alex and Lee take turns, with Alex starting first.  Initially, M = 1.
# On each player's turn, that player can take all the stones in the first X remaining piles, where 1 <= X <= 2M.  Then, we set M = max(M, X).
# The game continues until all the stones have been taken.
# Assuming Alex and Lee play optimally, return the maximum number of stones Alex can get.
 # Example 1:
# Input: piles = [2,7,9,4,4]
# Output: 10
# Explanation:  If Alex takes one pile at the beginning, Lee takes two piles, then Alex takes 2 piles again. Alex can get 2 + 4 + 4 = 10 piles in total. If Alex takes two piles at the beginning, then Lee can take all three piles left. In this case, Alex get 2 + 7 = 9 piles in total. So we return 10 since it's larger. 
 # Constraints:
# 1 <= piles.length <= 100
# 1 <= piles[i] <= 10 ^ 4

#
# @lc app=leetcode id=1140 lang=python3
#
# [1140] Stone Game II
#
class Solution:
    def stoneGameII(self, A: List[int]) -> int:
        N = len(A)
        for i in range(N - 2, -1, -1):
            A[i] += A[i + 1]
        from functools import lru_cache
        # lru_cache 
        # Decorator to wrap a function with a memoizing callable 
        # that saves up to the maxsize most recent calls. 
        # It can save time when an expensive or 
        # I/O bound function is periodically called with the same arguments.
        @lru_cache(None)
        def dp(i, m):
            if i + 2 * m >= N:
                return A[i]
            return A[i] - min(dp(i + x, max(x, m)) for x in range(1, 2 * m + 1))

        return dp(0, 1)

