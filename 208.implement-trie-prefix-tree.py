#
# @lc app=leetcode id=208 lang=python3
#
# [208] Implement Trie (Prefix Tree)
#
# https://leetcode.com/problems/implement-trie-prefix-tree/description/
#
# algorithms
# Medium (39.82%)
# Likes:    1864
# Dislikes: 34
# Total Accepted:    202.4K
# Total Submissions: 498.2K
# Testcase Example:  '["Trie","insert","search","search","startsWith","insert","search"]\n[[],["apple"],["apple"],["app"],["app"],["app"],["app"]]'
#
# Implement a trie with insert, search, and startsWith methods.
# 
# Example:
# 
# 
# Trie trie = new Trie();
# 
# trie.insert("apple");
# trie.search("apple");   // returns true
# trie.search("app");     // returns false
# trie.startsWith("app"); // returns true
# trie.insert("app");   
# trie.search("app");     // returns true
# 
# 
# Note:
# 
# 
# You may assume that all inputs are consist of lowercase letters a-z.
# All inputs are guaranteed to be non-empty strings.
# 
# 
#

import collections

class LinkNode():
    def __init__(self, *args, **kwargs):
        self.child = collections.defaultdict(LinkNode)
        self.isEnd = False

class Trie:
    """
    Why Trie
        1. Finding all keys with a common prefix.
        2. Enumerating a dataset of strings in lexicographical order.

    Another reason why trie outperforms hash table, is that as hash table increases in size, 
    there are lots of hash collisions and the search time complexity could deteriorate to O(n), 
    where n is the number of keys inserted. 
    Trie could use less space compared to Hash Table when storing many keys with the same prefix. 
    In this case using trie has only O(m) time complexity, 
    where m is the key length. 
    Searching for a key in a balanced tree costs O(mlogn) time complexity.
    """
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = LinkNode()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        node = self.root

        for c in word:
            node = node.child[c]
        
        node.isEnd = True
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        node = self.root
        for c in word:
            node = node.child.get(c)
            if node is None: return False

        return node.isEnd
        

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        node = self.root
        for c in prefix:
            node = node.child.get(c)
            if node is None: return False
        return True
# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

