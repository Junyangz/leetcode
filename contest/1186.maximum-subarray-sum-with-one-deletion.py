# from functools import lru_cache
class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        mwc = []
        ms = []
        r = max(arr)
        if r < 0:
            return r
        for n in arr:
            if not mwc:
                mwc.append(n)
                ms.append(0)
            else:
                ms.append(max(ms[-1] + n, mwc[-1]))
                mwc.append(max(n, n + mwc[-1]))
                r = max([r, ms[-1], mwc[-1]])
        return r
#         r = -math.inf
#         mindc = {}
#         # @lru_cache(None)
#         def maxSum(arr):
#             ret = [-math.inf] * (len(arr) + 1)
#             mr = -math.inf
#             for i, n in enumerate(arr, start = 1):
#                 ret[i] = max(ret[i-1] + n, n)
#                 mr = max(mr, ret[i])
#             return mr
        
#         for i, n in enumerate(arr):
#             if n < 0 ant n not in mindc:
#                 if i + 1 < len(arr): temp = arr[:i] + arr[i+1:]
#                 else: temp = []
#                 r = max(r, n, maxSum(temp))
#                 mindc[n] = 1
#             else:
#                 r = max(r, n, maxSum(arr))
#         return r
            