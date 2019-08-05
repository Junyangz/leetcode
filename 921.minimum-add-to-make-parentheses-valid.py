#
# @lc app=leetcode id=921 lang=python3
#
# [921] Minimum Add to Make Parentheses Valid
#
class Solution:
    def minAddToMakeValid(self, S: str) -> int:
        # stack = []
        # for p in S:
        #     if stack and stack[-1] == '(' and p == ')':
        #         stack.pop()
        #     else:
        #         stack.append(p)
        # return len(stack)
        # ans = bal = 0
        # for symbol in S:
        #     bal += 1 if symbol == '(' else -1
        #     # It is guaranteed bal >= -1
        #     if bal == -1:
        #         ans += 1
        #         bal += 1
        # return ans + bal  
        left = right = 0
        for i in S:
            if right == 0 and i == ')':
                left += 1
            else:
                right += 1 if i == '(' else -1
        return left + right

