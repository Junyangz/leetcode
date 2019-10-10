# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def twoSumBSTs(self, root1: TreeNode, root2: TreeNode, target: int) -> bool:
        able_node = []
        def node_traversl(node):
            if node:
                able_node.append(target - node.val)
                node_traversl(node.left)
                node_traversl(node.right)
        
        self.find = False
        def find_able(node):
            if node:
                if node.val in able_node:
                    self.find = True
                find_able(node.left)
                find_able(node.right)
        
        node_traversl(root1)
        find_able(root2)
        
        return self.find