#
# @lc app=leetcode id=572 lang=python3
#
# [572] Subtree of Another Tree
#
# https://leetcode.com/problems/subtree-of-another-tree/description/
#
# algorithms
# Easy (42.01%)
# Likes:    1380
# Dislikes: 52
# Total Accepted:    120.5K
# Total Submissions: 285.1K
# Testcase Example:  '[3,4,5,1,2]\n[4,1,2]'
#
# 
# Given two non-empty binary trees s and t, check whether tree t has exactly
# the same structure and node values with a subtree of s. A subtree of s is a
# tree consists of a node in s and all of this node's descendants. The tree s
# could also be considered as a subtree of itself.
# 
# 
# Example 1:
# 
# Given tree s:
# 
# ⁠    3
# ⁠   / \
# ⁠  4   5
# ⁠ / \
# ⁠1   2
# 
# Given tree t:
# 
# ⁠  4 
# ⁠ / \
# ⁠1   2
# 
# Return true, because t has the same structure and node values with a subtree
# of s.
# 
# 
# Example 2:
# 
# Given tree s:
# 
# ⁠    3
# ⁠   / \
# ⁠  4   5
# ⁠ / \
# ⁠1   2
# ⁠   /
# ⁠  0
# 
# Given tree t:
# 
# ⁠  4
# ⁠ / \
# ⁠1   2
# 
# Return false.
# 
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # def isMatch(self, s: TreeNode, t: TreeNode)-> bool:
    #     if not (s and t):
    #         return s is t
    #     if not s: return False
    #     return s.val == t.val and self.isMatch(s.left, t.left) and self.isMatch(s.right, t.right)

    # def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
    #     if self.isMatch(s, t): return True
    #     if not s: return False
        
    #     return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)
        
    def isSubtree(self, s, t):
        from hashlib import sha256
        def hash_(x):
            x = x.encode()
            S = sha256()
            S.update(x)
            return S.hexdigest()
            
        def merkle(node):
            if not node:
                return '#'
            m_left = merkle(node.left)
            m_right = merkle(node.right)
            node.merkle = hash_(m_left + str(node.val) + m_right)
            return node.merkle
            
        merkle(s)
        merkle(t)
        def dfs(node): 
            if not node:
                return False
            return (node.merkle == t.merkle or 
                    dfs(node.left) or dfs(node.right))
                        
        return dfs(s)
