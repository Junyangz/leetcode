import collections
class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        return  max(collections.Counter([tuple(i ^ m[0] for i in m) for m in matrix]).values())