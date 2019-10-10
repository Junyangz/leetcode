from functools import lru_cache
class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:
        self.found = False
        if k == len(s) or k == len(s) - 1: return True
        #  使用lru_cache是通过的关键，不用就超时。
        @lru_cache(None)
        def find_p(s, m):
            if m < 0:
                return 
            n = len(s)
            if n == 1 or n == 0:
                self.found = True
                
            if n >= 2 and m >= 0 and not self.found:
                if s[0] == s[-1]:
                    find_p(s[1:-1], m)
                else:
                    if m - 1 >= 0:
                        find_p(s[:-1], m - 1)
                        find_p(s[1:], m - 1)
        find_p(s, k)
        
        return self.found

# top 1 solution
#     from functools import lru_cache
# class Solution:
#     def isValidPalindrome(self, s: str, k: int) -> bool:
#         n = len(s)
#         t = s[::-1]
#         @lru_cache(None)
#         def dp(i, j):
#             if i == 0 or j == 0:
#                 return i + j
#             i-=1;j-=1
#             if s[i] == t[j]: return dp(i, j)
#             return 1 + min(dp(i+1,j), dp(i,j+1))
        
#         return dp(n, n) <= 2 * k