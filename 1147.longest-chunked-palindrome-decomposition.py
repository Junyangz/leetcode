class Solution:
    def longestDecomposition(self, T: str) -> int:
        d = collections.deque(list(T))
        left = collections.deque([])
        right = collections.deque([])
        res = 0
        while len(d) // 2 > 0:
            left.append(d.popleft())
            right.appendleft(d.pop())
            if left == right:
                res += 2
                left = collections.deque([])
                right = collections.deque([])
        return res + 1 if len(d) or len(left) or len(right) else res

        # res, l, r = 0, "", ""
        # for i, j in zip(T, T[::-1]):
        #     l, r = l + i, j + r
        #     if l == r:
        #         res, l, r = res + 1, "", ""
        # return res

        