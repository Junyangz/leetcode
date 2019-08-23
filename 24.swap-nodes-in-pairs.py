#
# @lc app=leetcode id=24 lang=python3
#
# [24] Swap Nodes in Pairs
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        curr, pre, tmp = head, None, head
        for i in range(2):
            if not tmp: return head
            result = tmp
            tmp = tmp.next
            if curr!= None:
                next = curr.next
                curr.next = pre
                pre = curr
                curr = next

        head.next = self.swapPairs(curr)
        return result
