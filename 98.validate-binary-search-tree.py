#
# @lc app=leetcode id=98 lang=python3
#
# [98] Validate Binary Search Tree
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode, lower=-math.inf, upper=math.inf) -> bool:
        if root is None:
            return True
        if root.val <= lower or root.val >= upper: return False
        return self.isValidBST(root.left, lower, root.val) and self.isValidBST(root.right, root.val, upper)
