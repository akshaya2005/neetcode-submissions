class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        res = []
        prereqs = defaultdict(list)
        for course, prereq in prerequisites:
            prereqs[course].append(prereq)
        
        visited, cycle = set(), set()
        def dfs(curr):
            if curr in cycle:
                return False
            if curr in visited:
                return True

            cycle.add(curr)
            for child in prereqs[curr]:
                if dfs(child) == False:
                    return False
            cycle.remove(curr)
            visited.add(curr)
            res.append(curr)
            return True
        
        
        for i in range(numCourses):
            if dfs(i) == False:
                return []
        return res


        