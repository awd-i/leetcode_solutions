# Last updated: 11/11/2025, 1:56:06 AM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0
        def dfs(node):
            if not node:
                return -1
            nonlocal diameter
            left_path = dfs(node.left)
            right_path = dfs(node.right)
            diameter = max(diameter, left_path + 1 + right_path + 1)
            return max(left_path, right_path) + 1
        dfs(root)
        return diameter
