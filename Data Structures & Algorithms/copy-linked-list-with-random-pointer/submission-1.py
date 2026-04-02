"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        
        listMap = {}
        listHead = head

        while listHead:
            listMap[listHead] = Node(listHead.val)
            listHead = listHead.next

        listHead = head

        while listHead:
            if listHead.next:
                listMap[listHead].next = listMap[listHead.next]
            if listHead.random:
                listMap[listHead].random = listMap[listHead.random]
            listHead = listHead.next
        
        return listMap[head]