class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = [i for i in range(len(edges) + 1)]
        rank = [1] * (len(edges) + 1)
        def find(i):
            root = parent[i]
        
            # Path Compression
            if parent[root] != root:
                parent[i] = find(root)
                return parent[i]
        
            return root

        def unionSets(x, y):
            xRoot = find(x)
            yRoot = find(y)

            if xRoot == yRoot:
                return False

            # Union by Rank   
            if rank[xRoot] > rank[yRoot]:
                parent[yRoot] = xRoot
                rank[xRoot] += rank[yRoot]
            else:
                parent[xRoot] = yRoot
                rank[yRoot] += rank[xRoot]
            return True
        
    
        for u, v in (edges):
            if not unionSets(u, v):
                return [u, v]
            
        



        