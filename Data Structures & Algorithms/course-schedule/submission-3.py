class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = defaultdict(list)
        visited = set()


        for crse, pre in prerequisites:
            preMap[crse].append(pre)


        def dfs(crse):
            if crse in visited:
                return False

            if preMap[crse] ==[]:
                return True
            visited.add(crse)

            for pre in preMap[crse]:
                if not dfs(pre):
                    return False

            visited.remove(crse)
            preMap[crse] = []
            return True        
                      
        for crse in range(numCourses):
            if not dfs(crse):
                return False
        return True          