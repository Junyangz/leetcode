#
# @lc app=leetcode id=264 lang=python3
#
# [264] Ugly Number II
#
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        count = 1
        dp = [1] * n
        i = j = k = 0
        
        while count < n:
            minu = min(dp[i] * 2, dp[j] * 3, dp[k] * 5)
            if minu == dp[i] * 2: i += 1
            if minu == dp[j] * 3: j += 1
            if minu == dp[k] * 5: k += 1
            dp[count] = minu
            count += 1

        return dp[-1]

