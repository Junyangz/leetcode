#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#
from functools import lru_cache
class Solution:
    @lru_cache(None)
    def climbStairs(self, n: int) -> int:
        if n <= 3: return n
        return self.climbStairs(n-1) + self.climbStairs(n-2)
        
        #dp
        # if n <= 3: return n
        # dp = [0] * (n + 2)
        # dp[1]  = 1
        # dp[2]  = 2
        # for i in range(3, n+1):
        #     dp[i] = dp[i-1] + dp[i-2]
        # return dp[n]
