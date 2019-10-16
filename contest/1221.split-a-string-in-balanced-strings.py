class Solution:
    def balancedStringSplit(self, S: str) -> int:
        ans = 0
        bal = 0
        for c in S:
            bal += 1 if c == 'L' else -1
            if bal == 0: ans += 1
        return ans