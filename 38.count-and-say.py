#
# @lc app=leetcode id=38 lang=python
#
# [38] Count and Say
#
class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        s = '1'
        def cs(s):
            rstr = ''
            tc, tempc = 1, s[0]
            for i in range(1,len(s)):
                if s[i] == tempc:
                    tc += 1
                else:
                    rstr = rstr + str(tc) + tempc
                    tempc = s[i]
                    tc = 1
            rstr = rstr + str(tc) + tempc
            return rstr

        for _ in range(n-1):
            s = cs(list(s))
        return s
