class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereqs = {i:[] for i in range(numCourses)}

        for course, prereq in prerequisites:
            prereqs[course].append(prereq)

        visits = set()
        
        def dfs(course):
            if course in visits:
                return False
            
            if prereqs[course] == []:
                return True
            
            visits.add(course)
            
            for prereq in prereqs[course]:
                if not dfs(prereq): return False
            visits.remove(course)
            prereqs[course] = []
            return True

        for course in range(numCourses):
            if not dfs(course): return False
        return True

