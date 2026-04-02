# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy
        carry = 0

        while l1 or l2:
            l1Val = 0
            l2Val = 0
            if l1:
                l1Val = l1.val
                l1 = l1.next
            if l2:
                l2Val = l2.val
                l2 = l2.next
            
            total = l1Val + l2Val + carry
            carry = total // 10
            digit = total % 10

            curr.next = ListNode(digit)
            curr = curr.next
        
        if carry == 1:
            curr.next = ListNode(1)

        return dummy.next