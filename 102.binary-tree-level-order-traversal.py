#
# @lc app=leetcode id=102 lang=python3
#
# [102] Binary Tree Level Order Traversal
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    res = []
    def levelOrder(self, root: TreeNode, l=0) -> List[List[int]]:
        if not root: return None
        if l == 0: self.res = []
        if len(self.res) < l + 1: self.res.append([])
        self.res[l].append(root.val)
        left, right = self.levelOrder(root.left, l + 1), self.levelOrder(root.right, l + 1)         
        
        return self.res
