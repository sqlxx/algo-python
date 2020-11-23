# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if k == 1:
            return head
        
        j = k - 1
        validPoint = head
        while j > 0:
            if validPoint and validPoint.next:
                validPoint = validPoint.next 
                j -= 1
            else:
                return head
            
        def reverseK(begin:ListNode, num):
            i = num
            current = begin
            nextNode = begin.next
                
            while i > 0:
                if nextNode:
                    tmp = nextNode.next
                    nextNode.next = current
                    current = nextNode
                    nextNode = tmp 
                else:
                    break
                i -= 1
            begin.next = nextNode
            return current, begin 

        
        newHead, newEnd = reverseK(head, k-1)
        
        if newEnd and newEnd.next:
            newEnd.next = self.reverseKGroup(newEnd.next, k)

        return newHead
