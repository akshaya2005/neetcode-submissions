class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        ## make prereqs map 
        prereq = defaultdict(list)

        for crs, pre in prerequisites:
            prereq[crs].append(pre)
        
        visiting, visited = set(), set()
        res = []

        def dfs(crs):
            if crs in visiting:
                return False
            if crs in visited:
                return True
            ## visiting this node and checking for its prereqs
            ## cycle detection requires that you know whether the node was seen in *this* path
            visiting.add(crs)
            for pre in prereq[crs]:
                if not dfs(pre):
                    return False
            
            visiting.remove(crs)
            visited.add(crs)
            prereq[crs] = []
            res.append(crs)
            return True
        

        ## graph is disconnected so you have to do this
        for c in range(numCourses):
            if not dfs(c):
                return []
        
        return res