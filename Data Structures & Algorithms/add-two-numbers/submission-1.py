# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        cur = dummy
        carry = 0

        while l1 or l2 or carry != 0:
            # get l1/l2 values if they exist
            val1 = 0
            val2 = 0
            if l1:
                val1 = l1.val
                l1 = l1.next
            if l2:
                val2 = l2.val
                l2 = l2.next
            
            # get the right-most digit and carry (if any)
            total = val1 + val2 + carry
            carry = total // 10
            digit = total % 10
            
            # append new node
            cur.next = ListNode(digit, None)
            
            # move to next node
            cur = cur.next
        
        return dummy.next