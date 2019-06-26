#
# @lc app=leetcode id=23 lang=python3
#
# [23] Merge k Sorted Lists
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        ret = []
        for lst in lists:
            while lst:
                ret.append(lst.val)
                lst = lst.next
        return sorted(ret)

        # dummy = ListNode(None)
        # curr = dummy
        # q = PriorityQueue()
        # for node in lists:
        #     if node: q.put((node.val,node))
        # while q.qsize()>0:
        #     curr.next = q.get()[1]
        #     curr=curr.next
        #     if curr.next: q.put((curr.next.val, curr.next))
        # return dummy.next
