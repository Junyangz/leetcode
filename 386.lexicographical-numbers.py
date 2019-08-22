#
# @lc app=leetcode id=386 lang=python3
#
# [386] Lexicographical Numbers
#
class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        l = []
        curr = 1
        for i in range(1, n + 1):
            l.append(curr)
            if curr * 10 <= n:
                curr *= 10
            elif curr % 10 !=9 and curr + 1 <= n:
                curr += 1
            else:
                while (curr // 10) % 10 == 9:
                    curr = curr // 10
                curr = curr // 10 + 1
        return l
    #   hacky solution with less runtime and more memory
    #   return sorted([ x for x in range(1, n + 1) ], key = lambda x: str(x))    

