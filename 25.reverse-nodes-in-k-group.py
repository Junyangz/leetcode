#
# @lc app=leetcode id=25 lang=python3
#
# [25] Reverse Nodes in k-Group
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# review required 
# linknode reversed

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if not head or k == 1:
            return head
        tmp, prev, curr = head, None, head
        for _ in range(k):
            if not tmp: return head
            result = tmp
            tmp = tmp.next
        for _ in range(k):
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        head.next = self.reverseKGroup(curr, k)
        return result  

