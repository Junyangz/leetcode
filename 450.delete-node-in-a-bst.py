#
# @lc app=leetcode id=450 lang=python3
#
# [450] Delete Node in a BST
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    #     def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
    #         def dfs(node):
    #             if not node: return None
    #             left, right = dfs(node.left), dfs(node.right)
    #             if node.val == key:
    #                 if left and not right: 
    #                     node.left = None
    #                     node = left
    #                 elif right and not left:
    #                     node.right = None
    #                     node = right
    #                 elif not left and not right:
    #                     node = None
    #                 else:
    #                     node.right = None
    #                     node.val = right.val
    #                     node.left = left
                    
    #             return node
    #         return dfs(root)
    # BST TREE 左子树的值小于父节点，父节点的值小于右节点的值。
        def deleteNode(self, root, key):
            """
            :type root: TreeNode
            :type key: int
            :rtype: TreeNode
            """
            if not root:
                return
    
            if key > root.val:
                root.right = self.deleteNode(root.right, key)
                
            elif key < root.val:
                root.left = self.deleteNode(root.left, key)
            
            else:
                if not root.left:
                    return root.right
                else:
                    # try to find the max value on the left subtree
                    tmp = root.left
                    while tmp.right:
                        tmp = tmp.right
                    root.val = tmp.val
                    root.left = self.deleteNode(root.left, tmp.val)
            
            return root
                    

