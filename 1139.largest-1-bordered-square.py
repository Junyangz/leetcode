# review required
class Solution:
    def largest1BorderedSquare(self, A: List[List[int]]) -> int:
        m, n = len(A), len(A[0])

        top, left = [a[:] for a in A], [a[:] for a in A]
        for i in range(m):
            for j in range(n):
                if A[i][j]:
                    if i: top[i][j] = top[i - 1][j] + 1
                    if j: left[i][j] = left[i][j - 1] + 1
        for r in range(min(m, n), 0, -1):
            for i in range(m - r + 1):
                for j in range(n - r + 1):
                    if min(top[i + r - 1][j], top[i + r - 1][j + r - 1], left[i]
                           [j + r - 1], left[i + r - 1][j + r - 1]) >= r:
                        return r * r
        return 0
#         cur= [0, 0]
#         l = len(grid[0])
        
#         def check_vaild(x, y, length):
#             return sum([grid[x][i] for i in range(x, x+length)]) == sum(
#                 [grid[i][y] for i in range(y, y+length)]) == sum(
#                 [grid[x+length-1][i] for i in range(y, y+length)]) == sum(
#                 [grid[i][y+length-1] for i in range(x, x+length)]) == length
        
#         for i in range(l)
#             for x, y in range(i+1), range(i+1):
#                 if check_vaild(cur[0],cur[1],l):
#                     return l*l
#                 else:
#                     l -= 1