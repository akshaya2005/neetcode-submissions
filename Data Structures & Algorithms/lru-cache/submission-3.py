class LRUCache:
  
    class DLL:
        class Node:
            def __init__(self, key, val, prev, next):
                self.key = key
                self.val = val
                self.prev = prev
                self.next = next
            def __repr__(self):
                return f"Key: {self.key}, Val:{self.val}"

        def __init__(self):
            self.head = self.Node(0, 0, None, None)
            self.tail = self.Node(0, 0, None, None)
            self.head.next = self.tail
            self.tail.prev = self.head
        
        def remove(self, node):
            node.next.prev = node.prev
            node.prev.next = node.next


        def addToBack(self, node):
            self.tail.prev.next = node
            node.next = self.tail
            node.prev = self.tail.prev
            self.tail.prev = node
        
            
        def evict(self):
            removed = self.head.next
            self.head.next = self.head.next.next
            return removed
        
        def __repr__(self):
            string = ""
            curr = self.head
            while curr:
                string += f"Key: {curr.key}, Val: {curr.val} \n"
                curr = curr.next
            return string

    def __init__(self, capacity: int):
        self.cache = {} ## map key to node
        self.lru = self.DLL() ## map key to node
        self.capacity = capacity 
        

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1 
     
        self.lru.remove(self.cache[key])
        self.lru.addToBack(self.cache[key])
        return self.cache[key].val
        

    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            self.cache[key] = self.DLL.Node(key, value, None, None)
        else:
            self.cache[key].val = value
            self.lru.remove(self.cache[key])
        
        self.lru.addToBack(self.cache[key])
        if len(self.cache) > self.capacity:
            lru = self.lru.head.next
            self.lru.remove(lru)
            del self.cache[lru.key]
       

        
