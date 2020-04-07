# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return None
        prev = head
        current = head.next
        while current:
            while current and prev.val == current.val:
                current = current.next

            prev.next = current
            if not current:
                return head
            
            prev = current
            current = current.next
        
        return head
                
            
