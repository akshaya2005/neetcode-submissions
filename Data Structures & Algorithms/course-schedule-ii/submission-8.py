class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereqs = defaultdict(list)
        for crs, pre in prerequisites:
            prereqs[crs].append(pre)
        
        visiting = set()
        visited = set()

        res = []

        def dfs(crs):
            if crs in visited:
                return True
            if crs in visiting:
                return False
            
            visiting.add(crs)
            for pre in prereqs[crs]:
                ## if any of the children
                ## are part of a cycle return false
                if not dfs(pre):
                    return False
            visiting.remove(crs)
            visited.add(crs)

            res.append(crs)
            ## this course was successfully visitd without 
            ## finding a cycle 
            return True
        
        for c in range(numCourses):
            ## a cycle was found containing c
            if not dfs(c):
                return []
        
        return res
            
