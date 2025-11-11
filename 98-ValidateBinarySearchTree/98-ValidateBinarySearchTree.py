# Last updated: 11/11/2025, 1:57:45 AM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:


        def dfs(node, high, low):
            if not node:
                return True

            if not (low < node.val < high):
                return False

            return (dfs(node.left, node.val, low) and dfs(node.right, high, node.val))

    
        return dfs(root, float('inf'), float('-inf'))