# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# Intuition
# parent, left child and right child, the second player choose one of it will get all of them subtree with the one as root, so if there any subtree
# node number greater than half of all the node, the second player will win.

#
# The first player colors a node,
# there are at most 3 nodes connected to this node.
# Its left, its right and its parent.
# Take this 3 nodes as the root of 3 subtrees.

# The second player just color any one root,
# and the whole subtree will be his.
# And this is also all he can take,
# since he cannot cross the node of the first player.

class Solution:
    def btreeGameWinningMove(self, root: TreeNode, n: int, x: int) -> bool:
        pre = [0, 0]
        
        def count(node):
            if not node: return 0
            left, right = count(node.left), count(node.right)
            if node.val == x:
                pre[0], pre[1] = left, right
            return left + right + 1
        
        return count(root) // 2  < max(n - sum(pre) - 1, pre[0], pre[1])
        