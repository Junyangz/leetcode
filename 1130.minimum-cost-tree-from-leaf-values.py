import math
class Solution0:
    def mctFromLeafValues(self, A: List[int]) -> int:
        stack = [math.inf]
        rs = 0
        for a in A:
            while stack[-1] < a:
                mid = stack.pop()
                rs += min(a, stack[-1]) * mid
            stack.append(a)
        while len(stack) > 2:
            rs += stack.pop() * stack[-1]

        return rs

class Solution1:
    def mctFromLeafValues(self, A: List[int]) -> int:
        rs = 0
        for a in sorted(A)[:-1]:
            i = A.index(a)
            left = A[i - 1] if i > 0 else math.inf
            right = A[i + 1] if i+1 < len(A) else math.inf
            rs += min(left, right) * a
            A.pop(i)
        return rs