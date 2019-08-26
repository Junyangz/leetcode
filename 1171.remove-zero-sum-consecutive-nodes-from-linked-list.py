# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeZeroSumSublists(self, head: ListNode) -> ListNode:
        # awesome solution from lee
        '''
        1. how to remove zero sum consecutive value from an array
            1.1 scan from left and calculate the prefix sum
            1.2 whenever meet the seen prefix(means that sum value from previous prefix to now is zero)
            1.3 remove all elements of the subarry between them
        2. change it to Linked list
            2.1 as head listnode can be removed in the end, a dummy Listnode set as the head previous node.
            2.2 hashmap stored the prefix sum as key the related node as value.
        '''
        curr = dummy = ListNode(0)
        prefix = 0
        is_seen = collections.OrderedDict()
        curr.next = head
        while curr:
            prefix += curr.val
            node = is_seen.get(prefix, curr)

            while prefix in is_seen:
                is_seen.popitem()

            is_seen[prefix] = node
            node.next = curr = curr.next

        return dummy.next

        # cur = dummy = ListNode(0)
        # dummy.next = head
        # prefix = 0
        # seen = collections.OrderedDict()
        # while cur:
        #     prefix += cur.val
        #     node = seen.get(prefix, cur)
        #     while prefix in seen:
        #         seen.popitem()
        #     seen[prefix] = node
        #     node.next = cur = cur.next
        # return dummy.next