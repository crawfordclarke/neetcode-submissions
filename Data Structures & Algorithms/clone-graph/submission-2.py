"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        node_map = {}

        def dfs(node):

            if not node: return None

            if node in node_map:
                return node_map[node]

            clone = Node(node.val)
            node_map[node] = clone

            for neighbor in node.neighbors:
                clone_neighbor = dfs(neighbor)
                clone.neighbors.append(clone_neighbor)
            return clone


        return dfs(node)

