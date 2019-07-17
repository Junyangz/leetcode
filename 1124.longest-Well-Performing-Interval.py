import bisect
class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        stack = [[0,0]]
        res = cur = 0
        for i, h in enumerate(hours, 1):
            if h > 8:
                cur -= 1
            else:
                cur += 1
            j = bisect.bisect(stack, [cur + 1])
            print(j,cur,i)
            if j < len(stack):
                res = max(res, i - stack[j][1])
            if stack[-1][0] < cur:
                stack.append([cur, i])
            print(res,stack)
        return res
        