
class Solution:
    class DSU:
        def __init__(self, size):
            ## start with each node being its own parent
            self.parent = [i for i in range(size+1)]
            ## each node also has a rank of 1 since each
            ## disjoint set only consists of a single vertex
            self.rank = [1 for _ in range(size+1)]
        def find(self, node):
            if self.parent[node] != node:
                return self.find(self.parent[node])
            return node
        
        def union(self, a, b):
            aPar = self.find(a)
            bPar = self.find(b)
            if aPar == bPar:
                return False
            if self.rank[aPar] > self.rank[bPar]:
                self.parent[bPar] = aPar
                self.rank[aPar] += self.rank[bPar]
            else:
                self.parent[aPar] = bPar
                self.rank[bPar] += self.rank[aPar]
            return True

    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        unionFind = self.DSU(n)

        for u, v in edges:
            ## these vertices have been unioned already
            if not unionFind.union(u, v):
                return [u, v]
        

