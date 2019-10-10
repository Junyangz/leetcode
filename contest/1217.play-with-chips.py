class Solution:
    def minCostToMoveChips(self, chips: List[int]) -> int:
        # can't understand the problem😳
        c = [0, 0]
        for x in chips: 
            c[x % 2] += 1
        return min(c)