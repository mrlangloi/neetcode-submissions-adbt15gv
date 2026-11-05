# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return None
        
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        tempHead = slow.next
        tempPrev = None
        slow.next = None
        
        while tempHead:
            tempNext = tempHead.next
            tempHead.next = tempPrev
            tempPrev = tempHead
            tempHead = tempNext
        
        dummy = head

        while tempPrev:
            temp1 = dummy.next
            temp2 = tempPrev.next
            dummy.next = tempPrev
            tempPrev.next = temp1
            dummy = temp1
            tempPrev = temp2