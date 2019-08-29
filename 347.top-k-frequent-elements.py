#
# @lc app=leetcode id=347 lang=python3
#
# [347] Top K Frequent Elements
#

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #return sorted(collections.Counter(nums).keys(), key=collections.Counter(nums).get, reverse=True)[:k]
        return heapq.nlargest(k, collections.Counter(nums).keys(), key=collections.Counter(nums).get)

