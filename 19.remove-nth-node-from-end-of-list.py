#
# @lc app=leetcode id=19 lang=python3
#
# [19] Remove Nth Node From End of List
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        start = nth = dummy
        for _ in range(n + 1):
            start = start.next

        while start:
            start = start.next
            nth = nth.next

        nth.next = nth.next.next

        return dummy.next
        

