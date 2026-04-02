# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        first = head
        count = 0

        while count < n:
            first = first.next
            count += 1
        
        second = head
        prev = None

        while first:
            prev = second
            first = first.next
            second = second.next
        
        if prev and second:
            prev.next = second.next
            return head
        else:
            return second.next
