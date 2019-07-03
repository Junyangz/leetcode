#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mP = 0
        
        if not prices:
            return 0
        else:
            m=prices[0]
            
        for i, s in enumerate(prices):
            mP = max(s-m, mP)
            if s < m:
                m = prices[i]
        return mP
