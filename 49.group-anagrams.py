#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        ret = collections.defaultdict(list)
        for ana in strs:
            ret[tuple(sorted(ana))].append(ana)
        return ret.values()
