class Solution:
    def lastSubstring(self, s: str) -> str:
        result=""
        for i in range(len(s)):
            # why brute force with max can pass, other language can't pass
            # Python3 AC, Python TLE.
            result=max(result,s[i:])
        return result