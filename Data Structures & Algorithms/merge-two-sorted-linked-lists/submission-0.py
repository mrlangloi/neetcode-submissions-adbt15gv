# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head1 = list1
        head2 = list2

        head = ListNode()
        tail = head

        # runs until either l1 or l2 hits end of list
        while head1 and head2 :
            if head1.val <= head2.val:
                tail.next = head1
                head1 = head1.next
            else:
                tail.next = head2
                head2 = head2.next
            tail = tail.next

        # append remainder of the unfinished list
        if head1:
            tail.next = head1
        else:
            tail.next = head2

        return head.next