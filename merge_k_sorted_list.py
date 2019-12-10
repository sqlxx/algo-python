# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        current = []
        head = resultCurrent = ListNode(0)
        
        for i in range(len(lists)):
            current.append(lists[i])
            

        def argmin(listCurrents:[ListNode]):
            
            currentVal = 9999999
            currentIdx = -1

            for i in range(len(listCurrents)):
                if listCurrents[i]:
                    if listCurrents[i].val < currentVal:
                        currentVal = listCurrents[i].val
                        currentIdx = i
            
            return currentIdx
        
        idx = argmin(current)
        while idx != -1:
            resultCurrent.next = current[idx]
            resultCurrent = current[idx]
            current[idx] = current[idx].next
            idx = argmin(current)

        return head.next