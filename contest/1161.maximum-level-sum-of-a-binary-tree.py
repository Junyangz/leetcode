# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxLevelSum(self, root: TreeNode, l = 0) -> int:
        minl = []
        def helper(node, l = 0):
            if not node: return 0
            left, right = helper(node.left, l + 1), helper(node.right, l + 1)
            while len(minl) < l + 1: minl.append(0)
            minl[l] += node.val
        helper(root, 0)
        # def helper2(node, l = 0):
        #     if node:
        #         yield node.val, l
        #         if node.left: yield from helper(node.left, l + 1)
        #         if node.right: yield from helper(node.right, l + 1)
        # for v in helper2(root, 0):
        #     print(v)
        return minl.index(max(minl)) + 1
        
        