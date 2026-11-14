class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjL = defaultdict(list)
        seen = set()
        processed = set()
        sol = []

        for crse, pre in prerequisites:
            adjL[crse].append(pre)


        def dfs(crse):
            if crse in seen:
                return False

            if crse in processed:
                return True
            seen.add(crse)

            for pre in adjL[crse]:
                if not dfs(pre):
                    return False

            seen.remove(crse)
            processed.add(crse)
            sol.append(crse)
            return True

        for crse in range(numCourses):
            if not dfs(crse):
                return []

        return sol            



                    
                    
            




        