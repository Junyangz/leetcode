#
# @lc app=leetcode id=108 lang=python3
#
# [108] Convert Sorted Array to Binary Search Tree
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBST(self, n: List[int]) -> TreeNode:
        if not n:
            return None
        
        mid = len(n) // 2
        root = TreeNode(n[mid])
        root.left = self.sortedArrayToBST(n[:mid])
        root.right = self.sortedArrayToBST(n[mid+1:])

        return root
