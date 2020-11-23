# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        
        result = ListNode(0)
        resultCurrent = result
        point1:ListNode = head
        point2:ListNode = None

        while point1 and point1.next:
            point2 = point1.next
            point1.next = point2.next
            resultCurrent.next = point2
            resultCurrent = point1
            point2.next = point1
            point1 = point1.next

        return result.next 
        