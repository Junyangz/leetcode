class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        n = len(s)
        A = [ abs(ord(s[i]) - ord(t[i])) for i in range(n) ]
        i = 0
        for j in range(n):
            maxCost -= A[j]
            if maxCost < 0:
                maxCost += A[i]
                i += 1
        return j - i + 1
        
        
        
        
        # N = len(S)
        # A = [abs(ord(S[i]) - ord(T[i])) for i in range(N)]
        # left = 0
        # windowsum = 0
        # ans = 0
        # for right, x in enumerate(A):
        #     windowsum += x
        #     while windowsum > maxCost and left < N:
        #         windowsum -= A[left]
        #         left += 1
        #     cand = right - left + 1
        #     ans = max(ans, cand)
        # return ans
    
#         save = maxCost
#         maxSub = 0
#         ret = 0
#         index = 0
        
#         for i, a in enumerate(s):
#             cost = abs(ord(a) - ord(t[i]))
#             if maxCost >= cost: 
#                 maxCost -= cost
#                 ret += 1
#                 index += 1
#             elif save >= cost:
#                 maxSub = max(ret, maxSub)
#                 maxCoust = save
#                 ret = 0
#                 continue
#             else:
#                 continue

#         return maxSub
    