# merge tow sorted linked list
# 2019-09-26 11:00:19 --- 58-interview-coding-test
# example: 
#    l1: 1->2->4
#    l2: 3->5->6
# Output: 1->2->3->4->5->6

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoSortedLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None or l2 is None:
            return l1 or l2
        dummy = cur = ListNode(0)
        while l1 and l2:
            cur.next = l1
            if l1.val < l2.val:
                l1 = l1.next
            else:
                tmp = l2.next
                cur.next = l2
                l2 = tmp
            cur = cur.next
        cur.next = l1 or l2
        return dummy.next