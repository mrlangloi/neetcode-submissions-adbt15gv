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
        nodes = {}

        tmp = head
        while tmp:
            nodes[tmp] = Node(tmp.val)
            tmp = tmp.next
        
        for k, v in nodes.items():
            v.next = nodes[k.next] if k.next else None
            v.random = nodes[k.random] if k.random else None

        return nodes[head] if head else None