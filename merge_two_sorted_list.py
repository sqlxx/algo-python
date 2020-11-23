# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        l1p = l1
        l2p = l2
        if l1p.val > l2p.val:
            head = l2p
            l2p = l2p.next
            current = head
        elif l1p.val == l2p.val:
            head = l1p
            tmp = l1p.next
            l1p.next = l2p
            l1p = tmp
            current = head.next
            l2p = l2p.next
        else:
            head = l1p
            l1p = l1p.next 
            current = head

        while l1p and l2p:
            if l1p.val > l2p.val:
                current.next = l2p
                current = l2p
                l2p = l2p.next
            else:
                current.next = l1p
                current = l1p
                l1p = l1p.next

        if l1p:
            current.next = l1p
        else:
            current.next = l2p
        return head