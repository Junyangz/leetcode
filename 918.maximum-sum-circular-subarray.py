#
# @lc app=leetcode id=918 lang=python3
#
# [918] Maximum Sum Circular Subarray
#
# need insight improve
import math
class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        totalSum, currmin, currmax= sum(A), math.inf, -math.inf
        maxSum, minSum = -math.inf, math.inf
        for a in A:
            currmin = min(currmin + a, a)
            minSum = min(minSum, currmin)
            currmax = max(currmax + a, a)
            maxSum = max(maxSum, currmax)
        
        return max(totalSum - minSum, maxSum) if maxSum > 0 else maxSum
        
#         total, maxSum, curMax, minSum, curMin = 0, -float('inf'), 0, float('inf'), 0
#         for a in A:
#             curMax = max(curMax + a, a)
#             maxSum = max(maxSum, curMax)
#             curMin = min(curMin + a, a)
#             minSum = min(minSum, curMin)
#             total += a
#         return max(maxSum, total - minSum) if maxSum > 0 else maxSum
    
#         def kadane(gen):
#             # Maximum non-empty subarray sum
#             ans = cur = -math.inf
#             for x in gen:
#                 cur = x + max(cur, 0)
#                 ans = max(ans, cur)
#                 print(ans)
#             return ans

#         S = sum(A)
#         ans1 = kadane(iter(A))
#         ans2 = S + kadane(-A[i] for i in range(1, len(A)))
#         ans3 = S + kadane(-A[i] for i in range(len(A) - 1))
#         return max(ans1, ans2, ans3)
#         A = [-math.inf] + A
#         n = len(A)
#         dp = [-math.inf] * n
#         for i in range(1, 2 * (n - 1)):
#             dp[i % n] = max(min(dp[i - 1] + A[i], sum(A[i- n // 2 + 1: i + 1])), A[i])
#         return max(dp)
    
    
    
#         A += A
#         dp = [ [-math.inf, 0] ] * len(A)
#         n = len(A)
#         print(dp)
#         for i in range(len(A)):
#             if dp[i][1] == 0:
#                 dp[i][0] = A[i]
#                 dp[i][1] += 1
#             else:
#                 if max(dp[::][1]) == n:
#                     break
#                 else:
#                     dp[i][0] = max(dp[i - 1][0]+ A[i], A[i])
#                     dp[i][1] += 1
       
#         #print(dp)
#         return max(dp[::][0])

