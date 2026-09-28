class Node:
    def __init__(self):
        self.children = [None for _ in range(26)]
        self.end = False
class PrefixTree:
    
    def __init__(self):
        self.root = Node()
    
    def search(self, word):
        curr = self.root
        for i in range(len(word)):
            index = ord(word[i]) - ord('a')
            if not curr.children[index]:
                return False
            curr = curr.children[index]
        return curr.end
    
    def insert(self, word):
        curr = self.root
        for i in range(len(word)):
            index = ord(word[i]) - ord('a')
            if not curr.children[index]:
                curr.children[index] = Node()
            curr = curr.children[index]
        curr.end = True
    
    def startsWith(self, prefix):
        curr = self.root
        for i in range(len(prefix)):
            index = ord(prefix[i]) - ord('a')
            if not curr.children[index]:
                return False
            curr = curr.children[index]
        return True 


        
        

