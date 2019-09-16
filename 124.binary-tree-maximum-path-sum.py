#
# @lc app=leetcode id=124 lang=python3
#
# [124] Binary Tree Maximum Path Sum
#
# https://leetcode.com/problems/binary-tree-maximum-path-sum/description/
#
# algorithms
# Hard (30.60%)
# Likes:    1981
# Dislikes: 149
# Total Accepted:    221.9K
# Total Submissions: 717.6K
# Testcase Example:  '[1,2,3]'
#
# Given a non-empty binary tree, find the maximum path sum.
# 
# For this problem, a path is defined as any sequence of nodes from some
# starting node to any node in the tree along the parent-child connections. The
# path must contain at least one node and does not need to go through the
# root.
# 
# Example 1:
# 
# 
# Input: [1,2,3]
# 
# ⁠      1
# ⁠     / \
# ⁠    2   3
# 
# Output: 6
# 
# 
# Example 2:
# 
# 
# Input: [-10,9,20,null,null,15,7]
# 
# -10
# / \
# 9  20
# /  \
# 15   7
# 
# Output: 42
# 
# 
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    current_max = -math.inf
    def maxPathSum(self, root: TreeNode) -> int:
        """
        :type root: TreeNode
        :rtype: int
        """
        self.maxPathSumHelper(root)
        return self.current_max

    def maxPathSumHelper(self, root):
        if root is None:
            return root
        left = self.maxPathSumHelper(root.left)
        right = self.maxPathSumHelper(root.right)
        left = 0 if left is None else (left if left > 0 else 0)
        right = 0 if right is None else (right if right > 0 else 0)
        self.current_max = max(left+right+root.val, self.current_max)
        return max(left, right) + root.val
