#
# @lc app=leetcode id=113 lang=python3
#
# [113] Path Sum II
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import copy
class Solution:
    def pathSum(self, root: TreeNode, S: int) -> List[List[int]]:
        if not root:
            return []
        if not root.left and not root.right and S == root.val:
            return [[root.val]]
        tmp = self.pathSum(root.left, S-root.val) + self.pathSum(root.right, S-root.val)
        return [[root.val]+i for i in tmp]
        # res = []
        # def helper(node, path):
        #     if node:
        #         path.append(node.val)
        #         if node.left or node.right:
        #             helper(node.left, copy.deepcopy(path))
        #             helper(node.right, copy.deepcopy(path))
        #         else:
        #             #print(path)
        #             if sum(path) == S:
        #                 res.append(path) 
        # helper(root, [])
        # return res
        

