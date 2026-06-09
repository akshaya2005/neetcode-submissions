class Node:
    def __init__(self, key, value):
        self.key = key
        self.val = value
        self.prev = None
        self.next = None

class LRUCache:
    
        
    
       ## doubly linked list
       ## pass in nodes for remove and insert
       ## map the keys to nodes in the cache
    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        ## head and tail
        ## not exactly they're dummy nodes
        ## marking the end and the beginning
        self.left = Node(0, 0)
        self.right = Node(0,0)
        ## doubly linking
        self.left.next, self.right.prev = self.right, self.left
    def remove(self, node: Node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev
    
    def add(self, node: Node):
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev
    

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.add(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.add(self.cache[key])

        if len(self.cache) > self.capacity:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
        

        

        
