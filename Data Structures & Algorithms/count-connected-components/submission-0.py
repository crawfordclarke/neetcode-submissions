class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        seen = set()
        islands = 0

        for node, neigh in edges:
            adj[node].append(neigh)
            adj[neigh].append(node)


        def dfs(node):
            if node in seen:
                return

            seen.add(node)    


            for neighbor in adj[node]:
                dfs(neighbor)


        for node in range(n):
            if not node in seen:
                dfs(node)
                islands += 1
        return islands        
        
