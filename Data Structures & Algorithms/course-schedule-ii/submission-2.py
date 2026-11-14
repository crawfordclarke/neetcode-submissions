class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjL = defaultdict(list)
        seen = set()
        sol = []


        for crse, pre in prerequisites:
            adjL[crse].append(pre)

        def dfs(crse):
            if crse in seen:
                return False

            if adjL[crse] == []:
                if crse not in sol:
                    sol.append(crse)
                return True    

            seen.add(crse)

            for pre in adjL[crse]:
                if not dfs(pre):
                    return False
                    
            seen.remove(crse)
            adjL[crse] = []
            sol.append(crse)
            return True

        for crse in range(numCourses):
            if not dfs(crse):
                return []

        return sol                


                    
                    
            




        