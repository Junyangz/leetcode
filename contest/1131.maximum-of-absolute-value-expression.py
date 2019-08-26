# review required
class Solution:
    def maxAbsValExpr(self, x: List[int], y: List[int]) -> int:
        res, n = 0, len(x)
        for p, q in [[1, 1], [1, -1], [-1, 1], [-1, -1]]:
            closest = p * x[0] + q * y[0] + 0
            for i in range(n):
                cur = p * x[i] + q * y[i] + i
                res = max(res, cur - closest)
                closest = min(closest, cur)
        return res