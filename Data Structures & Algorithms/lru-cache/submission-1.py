class ListNode:
    def __init__(self, key, val, next=None, prev=None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity

        # dummy head (mru), tail (lru) nodes
        self.head = ListNode(-1, -1)
        self.tail = ListNode(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def remove(self, node):
        prevNode = node.prev
        nextNode = node.next
        prevNode.next = nextNode
        nextNode.prev = prevNode
    
    def insert(self, node):
        prevNode = self.head
        nextNode = self.head.next
        node.prev = prevNode
        node.next = nextNode
        prevNode.next = node
        nextNode.prev = node

    def get(self, key: int) -> int:
        if key in self.cache:
            # get the node, remove it, add it back to the head
            node = self.cache[key]
            self.remove(node)
            self.insert(node)

            return self.cache[key].val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        node = ListNode(key, value)
        self.cache[key] = node
        self.insert(node)

        if len(self.cache) > self.capacity:
            # remove the lru node
            leastNode = self.tail.prev
            self.remove(leastNode)
            del self.cache[leastNode.key]



        
        
