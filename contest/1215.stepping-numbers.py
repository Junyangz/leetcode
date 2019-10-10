class Solution:
    def countSteppingNumbers(self, low: int, high: int) -> List[int]:
        ret = []
        # dfs may be more acceptable
        def bfs(n, m, num):
            stepNum = []
            stepNum.append(num)
            while stepNum:
                sn = stepNum.pop()

                if sn <= m and sn >= n:
                    ret.append(sn)
                if sn == 0 or sn > m:
                    continue
                last = sn % 10
                snA = sn * 10 + last - 1
                snB = sn * 10 + last + 1
                if last == 0:
                    stepNum.append(snB)
                elif last == 9:
                    stepNum.append(snA)
                else:
                    stepNum.append(snA)
                    stepNum.append(snB)
            return ret
        for i in range(10):
            bfs(low, high, i)
        ret.sort()
        return ret
#         ret = []
#         def isStepNum(n: int):
#             prev = -1
#             while n:
#                 curr = n % 10
#                 if prev == -1:
#                     prev = curr
#                 else:
#                     if abs(prev - curr) != 1:
#                         return False
#                 prev = curr
#                 n  = n // 10
#             return True
        
#         for i in range(low, high + 1):
#             if isStepNum(i):
#                 ret.append(i)
                
#         return ret