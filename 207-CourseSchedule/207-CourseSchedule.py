# Last updated: 11/11/2025, 1:57:20 AM
import collections
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courses = defaultdict(list)
        for a, b in prerequisites:
            courses[b].append(a)
        seen = set()
        path = set()

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
            return False

        for i in range(numCourses):
            if iscycle(i):
                return False
        return True
        




       
            

