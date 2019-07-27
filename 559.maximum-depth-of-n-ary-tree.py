"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root: return 0
        if not root.children: return 1
        return max(self.maxDepth(node) for node in root.children) + 1
    
#         def dfs(node, d):
#             temp = [0]
#             if not len(node.children):
#                 return d
#             else:
#                 for c in node.children:
#                     temp.append(dfs(c, d+1))
#                 return max(temp)
            
#         return dfs(root, 1) if root else 0
            