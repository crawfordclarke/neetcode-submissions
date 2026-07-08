# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:


        def equalNode(root1, root2):
            if not root1 and not root2:
                return True
            if not root1 or not root2:
                return False

            if root1.val != root2.val:
                return False
            
            equal = equalNode(root1.left, root2.left) and equalNode(root1.right, root2.right)
            return equal
        def dfs(root):
            if not root:
                return False

            # check if current node is the start of the subtree
            if equalNode(root, subRoot):
                return True
            
            # otherwise search left and right subtrees
            return dfs(root.left) or dfs(root.right)
        return dfs(root)


                
            
            
            
        