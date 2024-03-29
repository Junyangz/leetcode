#
# @lc app=leetcode id=146 lang=python3
#
# [146] LRU Cache
#
from collections import OrderedDict

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.cache: return -1
        val = self.cache[key]
        self.cache.move_to_end(key)
        return val

    def put(self, key: int, value: int) -> None:
        if key in self.cache: del self.cache[key]
        self.cache[key] = value
        if len(self.cache) > self.cap:
            self.cache.popitem(last=False)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
