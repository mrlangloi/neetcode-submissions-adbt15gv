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
        listMap = {None: None}
        listHead = head

        # 1st pass: create deep copies of each node
        while listHead:
            listMap[listHead] = Node(listHead.val)
            listHead = listHead.next

        listHead = head

        # 2nd pass: link each deep copies using original links
        while listHead:
            listMap[listHead].next = listMap[listHead.next]
            listMap[listHead].random = listMap[listHead.random]
            listHead = listHead.next
        
        return listMap[head]