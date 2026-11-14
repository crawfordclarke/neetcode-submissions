class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adjL = defaultdict(list)
        seen = set()


        for node,neigh in edges:
            adjL[node].append(neigh)
            adjL[neigh].append(node)


        def dfs(node, parent):
            if node in seen:
                return False
            

            seen.add(node)    

            for neigh in adjL[node]:
                if neigh == parent:
                    continue
                if not dfs(neigh, node):
                    return False    
            return True
        
        return dfs(0, -1) and len(seen) == n