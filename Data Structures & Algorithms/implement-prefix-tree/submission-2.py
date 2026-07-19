class PrefixTree:
    class TrieNode:
        
        def __init__(self):
            self.children = {}
            self.end = False

    def __init__(self):
        self.head = self.TrieNode()

    def insert(self, word: str) -> None:
        curr = self.head
        for char in word:
            if char not in curr.children:
                curr.children[char] = self.TrieNode()
            
            curr = curr.children[char]
        curr.end = True
    
        
    def search(self, word: str) -> bool:
        curr = self.head
        for char in word:
            if char not in curr.children:
                return False
            curr = curr.children[char]
     
        return curr.end
        

    def startsWith(self, prefix: str) -> bool:
        curr = self.head
        for char in prefix:
            if char not in curr.children:
                return False
            curr = curr.children[char]
        return True
        
        