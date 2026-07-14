# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        current_max = root.val



        def dfs(root, current_max):

            good = 0

            if not root:
                return 0
            
            
            good = 1 if root.val >= current_max else 0

            current_max = max(current_max, root.val)
            
            return good + dfs(root.left, current_max) + dfs(root.right, current_max)
        return dfs(root, current_max)
            

        