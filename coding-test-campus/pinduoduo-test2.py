class Solution():
    def maxPa(self, s: str)-> int:
        stack = []
        res = []
        maxRes = 0
        for i, x in enumerate(s):
            if not stack:
                stack.append(s)
            else:
                if stack[-1] == '(' and x == ')':
                    stack.pop()
                    res.append([i-1, i])
                    continue
                if stack[-1] == '[' and x == ']':
                    stack.pop()
                    res.append([i-1, i])
                    continue
                stack.append(x)

        if len(res) > 1:
            tmp = 2
            for i in range(1, len(res)):
                if res[i-1][1] == res[i][0]:
                    tmp += 2
                else:
                    maxRes = max(maxRes, tmp)
                    tmp = 2
            maxRes = max(maxRes, tmp)
        if len(res) == 1:
            maxRes = 2
            
        return maxRes


if __name__ == '__main__':

    test_case = input()
    s = Solution()
    print(s.maxPa(test_case))