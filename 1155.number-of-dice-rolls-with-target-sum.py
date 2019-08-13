class Solution:
    memo = {}
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        if (d, f, target) in self.memo:
            return self.memo[d, f, target]
        if d > target or target > d * f:
            return 0
        if d == 1:
            return 1
        self.memo[d, f, target] = sum(self.numRollsToTarget(d - 1, f, target - x) 
                                      for x in range(1, f + 1)) % (10 ** 9 + 7)
        
        return self.memo[d, f, target]

#    def numRollsToTarget(self, n: int, m: int, x: int) -> int:
        # table = [[0]*(x+1) for i in range(n+1)]

        # for j in range(1,min(m+1, x+1)):
        #     table[1][j] = 1

        # for i in range(2, n+1): 
        #     for j in range(1, x+1): 
        #         for k in range(1, min(m+1, j)): 
        #             table[i][j] += table[i-1][j-k] 

        # return table[-1][-1] % (10**9 + 7)