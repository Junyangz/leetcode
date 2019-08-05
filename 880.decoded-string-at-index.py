#
# @lc app=leetcode id=880 lang=python3
#
# [880] Decoded String at Index
#
class Solution:
    def decodeAtIndex(self, S: str, K: int) -> str:
        size = 0
        for e in S:
            if e.isdigit():
                size *= int(e)
            else:
                size += 1
        for c in reversed(S):
            K %= size
            if K == 0 and c.isalpha():
                return c
            
            if c.isdigit():
                size /= int(c)
            else:
                size -= 1
#         if K == 1: return S[0]
#         letter = collections.deque([''])
#         digit = collections.deque([])
#         for e in S:
#             if e in ['2','3','4','5','6','7','8','9']:
#                 letter.append('')
#                 digit.append(e)
#             else:
#                 letter[-1] += e
#         #letter.pop()   
#         while len(letter) and len(digit) and len(letter[0]) * int(digit[0]) < K:
#             l = letter.popleft() * int(digit.popleft())
#             if letter:
#                 l += letter.popleft()
#             letter.appendleft(l)
            
#         return letter[0][K % len(letter[0]) - 1]
                
               

