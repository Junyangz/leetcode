#
# @lc app=leetcode id=1029 lang=python3
#
# [1029] Two City Scheduling
#
class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        return sum([cost[i // (len(costs) // 2)] for i, cost in enumerate(sorted(costs, key= lambda cost: cost[0] - cost[1]))])

