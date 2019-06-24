#
# @lc app=leetcode id=897 lang=python3
#
# [897] Increasing Order Search Tree
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        def inorder(node):
            if node:
                yield from inorder(node.left)
                yield node.val#val not treenode 
                yield from inorder(node.right)
        
        ans = cur = TreeNode(None)
        
        for i in inorder(root):
            cur.right = TreeNode(i) #treenode not val
            cur = cur.right
        return ans.right

