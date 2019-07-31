#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#
class Solution:
    def threeSum(self, A: List[int]) -> List[List[int]]:
        if len(A) < 3: return None
        if len(A) == 3: return [sorted(A)] if sum(A) == 0 else None
        A.sort() #o(nlogn)
        N = len(A)
        res = []
        for i in range(N - 2):
            j = i + 1
            m = N - 1
            if A[i] == A[m] == 0: # fit with new testcase
                return [[0,0,0]]
            while j < m:
                tsum = A[i] + A[j] + A[m]
                if tsum == 0:
                    res.append((A[i], A[j], A[m])) # ??? (TLE)
                if tsum > 0:
                    m -= 1
                else:
                    j += 1
        return list(set(tuple(res))) # ??? (TLE)

