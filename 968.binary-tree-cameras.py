#
# @lc app=leetcode id=968 lang=python3
#
# [968] Binary Tree Cameras
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minCameraCover(self, root: TreeNode) -> int:
        # Set cameras on all leaves' parents, then remove all covered nodes.
        # Repeat step 1 until all nodes are covered.
        self.res = 0
        
        def dfs(root):
            if not root: return 2
            l, r = dfs(root.left), dfs(root.right)
            if l == 0 or r == 0:
                self.res += 1
                return 1
            return 2 if l == 1 or r == 1 else 0
        # if dfs(root) == 0 means that his left and right child all covered by their child, 
        # the root is the only one w/o covered, so root need install a camera.
        return (dfs(root) == 0) + self.res

