# Last updated: 11/11/2025, 1:57:18 AM
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        courses = defaultdict(list)
        for a, b in prerequisites:
            courses[b].append(a)
        
        seen = set()
        path = set()
        tgt = []

        def iscycle(curr):
            if curr in seen:
                return False
            if curr in path:
                return True
            
            path.add(curr)
            for child in courses[curr]:
                if iscycle(child):
                    return True
            
            path.remove(curr) 
            seen.add(curr)
            tgt.append(curr)
            return False
        

        for i in range(numCourses):
            if iscycle(i):
                return []
        return tgt[::-1]
        