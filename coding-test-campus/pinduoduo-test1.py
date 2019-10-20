class Solution():
    def minOpt(self, test_in: list)-> int:
        a, b = int(test_in[0]), int(test_in[-1])
        if a == b: return 0
        if a * b < 0 : return -1
        a, b = abs(a), abs(b)
        self.res = 0
        def dfs_10(a, i):
            if a == b: self.res = min(self.res, i) if self.res else i
            if a <= (b - 1) // 10:
                dfs_10(a * 10 + 1, i + 1)
                dfs_2(a * 10 + 1, i + 1)
            elif a * 2 <= b:
                dfs_10(a * 2, i + 1)
                dfs_2(a * 2, i + 1)
            else:
                pass
        def dfs_2(a, i):
            if a == b: self.res = min(self.res, i) if self.res else i
            if a * 2 <= b:
                dfs_2(a * 2, i + 1)
                dfs_10(a * 2, i + 1)
            if a <= (b - 1) // 10:
                dfs_10(a * 10 + 1, i + 1)
                dfs_2(a * 10 + 1, i + 1)
            else:
                pass
        dfs_10(a, 0)
        dfs_2(a, 0)
        return self.res if self.res else -1

if __name__ == '__main__':

    test_case = int(input())
    s = Solution()
    for _ in range(test_case):
        test_in = input().split()
        print(s.minOpt(test_in))
